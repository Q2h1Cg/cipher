#!/usr/bin/env python
# Written against python 3.3.1
# Matasano Problem 31
# Implement HMAC-SHA1 and break it with an artificial timing leak.
from prob18 import raw_xor
from prob1 import hexToRaw, rawToHex
from prob28 import sha1_from_github
import time
import os
import requests

def setByte(array, offset, value):
    array = array[0:offset] + value.to_bytes(1, byteorder='big') + array[offset+1:len(array)];
    return array

'''Things I learned doing this exercise:

Timing attacks are incredibly slow.  This takes around 3 hours to complete on
my machine.  There is an obvious way to make it 5x faster (1 trial instead of 5)
, but at the expense of accurancy (see next point).

The other thing I learned is how tempermental a timing attack can be.  If I start
this script and walk away, it finds the right answer.  If I start it and use my PC 
to browse the web, play or game, or hell, even just run the script inside of Eclipse,
it would eventually be led astray, maybe because of something the OS scheduler did?  
That's the reason for using 5 trials instead of one, but man does that take forever.'''


# The psuedocode on Wikipedia should be enough. HMAC is very easy.

BLOCKSIZE = 64;
DELAY = .05

def myhmac(hash_function, message, key):
    if (len(key) > BLOCKSIZE):
        key = hash(key)
    if (len(key) < BLOCKSIZE):
        key += (b'\x00' * (BLOCKSIZE - len(key)));

    opad = raw_xor(b'\x5c' * BLOCKSIZE, key);
    ipad = raw_xor(b'\x36' * BLOCKSIZE, key);
        
    return hash_function(opad + hexToRaw(hash_function(ipad + message)));
        

def test_hmac():
    #HMAC_SHA1("", "") = 0xfbdb1d1b18aa6c08324b7d64b71fb76370690e1d
    #HMAC_SHA1("key", "The quick brown fox jumps over the lazy dog") = 0xde7c9b85b8b78aa6bc8a7a36f70a90701c9db4d9
    keys = [b'', b'key']
    messages = [b'', b'The quick brown fox jumps over the lazy dog'];
    answers = ['fbdb1d1b18aa6c08324b7d64b71fb76370690e1d',
               'de7c9b85b8b78aa6bc8a7a36f70a90701c9db4d9']
    for i in range(len(keys)):
        if (myhmac(sha1_from_github, messages[i], keys[i]) != answers[i]):
            print("hmac error");
            exit(-1);
    
'''Using the web framework of your choosing (Sinatra, web.py, whatever),
write a tiny application that has a URL that takes a "file" argument
and a "signature" argument, like so:

http://localhost:9000/test?file=foo&signature=46b4ec586117154dacd49d664e5d63fdc88efb51

Have the server generate an HMAC key, and then verify that the
"signature" on incoming requests is valid for "file", using the "=="
operator to compare the valid MAC for a file with the "signature"
parameter (in other words, verify the HMAC the way any normal
programmer would verify it).

Write a function, call it "insecure_compare", that implements the ==
operation by doing byte-at-a-time comparisons with early exit (ie,
return false at the first non-matching byte).

In the loop for "insecure_compare", add a 50ms sleep (sleep 50ms after
each byte).

Use your "insecure_compare" function to verify the HMACs on incoming
requests, and test that the whole contraption works. Return a 500 if
the MAC is invalid, and a 200 if it's OK.
'''

# Using the timing leak in this application, write a program that
# discovers the valid MAC for any file.                
def discover_mac(message):
    guess_mac = b'\x00' * 20;
    for i in range(20):
        nextbyte = guess_byte(message, i, guess_mac);
        guess_mac = setByte(guess_mac, i, nextbyte);
    print (rawToHex(guess_mac));
    return guess_mac;


def guess_byte(message, index, guess_mac, numtrials=1):
    timings = [0]*256;
    # try each byte at the index
    for i in range(256):
        this_guess = setByte(guess_mac, index, i);
        url = b'http://127.0.0.1:9000/test?file=' + message + b'&signature=' + rawToHex(this_guess);
        #print(url)
        start = time.perf_counter()
        requests.get(url);        
        stop = time.perf_counter()
        timings[i] = stop - start;
    # assume the largest timing is the right one
    # for i in range(len(timings)):
    #     print(i,timings[i])
    value = timings.index(max(timings));
    print("index: " + str(index) + " : value: " + hex(value));
    return value;


def do31():
    test_hmac();
    #startserver(DELAY);
    #known answer: b'6262261f054f0a17dfa68d87bf64f5416c128340'
    discover_mac(b'Mary had a little lamb');

#6262261f054f0a17dfa68d87bf64f5416c128340
#1111111111111111111111111111111111111111

if __name__ == "__main__":
    do31();
    os._exit(0);