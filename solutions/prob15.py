#!/usr/bin/env python
# Written against python 3.3.1
# Matasano Problem 15
# PKCS#7 padding validation

# Write a function that takes a plaintext, determines if it has valid
# PKCS#7 padding, and strips the padding off.

def checkAndRemovePKCS7Padding(raw):
    padLen = raw[len(raw)-1];
    expectedPadding = bytes(chr(padLen), 'UTF-8') * padLen;
    actualPadding = raw[(-1*padLen):];
    if (expectedPadding != actualPadding):
        raise ValueError("Pad padding");
    return raw[0:len(raw)-padLen];



if __name__ == "__main__":
    good1 = b'ICE ICE BABY\x04\x04\x04\x04'
    print(checkAndRemovePKCS7Padding(good1))
