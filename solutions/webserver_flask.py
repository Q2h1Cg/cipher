#!/usr/bin/env python
# Written against python 3.3.1
# Simple web server to for problems 31/32
# Got tired of tryiing to install 
# non-python3 compatible web frameworks

from flask import Flask, request 
from prob1 import hexToRaw
from prob28 import sha1_from_github
from prob18 import raw_xor
import time

RESPONSE_500 = b'HTTP/1.1 500 Internal Server Error\n'
RESPONSE_200 = b'HTTP/1.1 200 OK\n'
COMPARE_DELAY = 0.05

HMAC_KEY = b'YELLOW SUBMARINE'


app = Flask(__name__)

@app.route("/test")
def test():
	file_value = bytes(request.args.get("file"),'utf-8');
	signature_hex = bytes(request.args.get("signature"),'utf-8');
	computed_signature_hex = myhmac(sha1_from_github, file_value, HMAC_KEY);
	print(computed_signature_hex)
	if (insecure_equals(hexToRaw(signature_hex), hexToRaw(computed_signature_hex))):
		return RESPONSE_200
	else:
		return RESPONSE_500

BLOCKSIZE = 64
def myhmac(hash_function, message, key):
    if (len(key) > 64):
        key = hash(key)
    if (len(key) < 64):
        key += (b'\x00' * (64 - len(key)));

    opad = raw_xor(b'\x5c' * 64, key);
    ipad = raw_xor(b'\x36' * 64, key);
    return (hash_function(opad + hexToRaw(hash_function(ipad + message))));

def insecure_equals(this, that):
    print(this,that)
    if (len(this) != len(that)):
        return False;
    for i in range(len(this)):
        if (this[i] != that[i]):
            return False;
        time.sleep(COMPARE_DELAY);
    return True;

if __name__ == '__main__':
	app.run(port=9000)