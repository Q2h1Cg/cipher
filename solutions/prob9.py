#!/usr/bin/env python
# Written against python 3.3.1
# Matasano Problem 8
# Implement PKCS#7 padding

def addPKCS7Padding(data, blocksize):
    numBytes = blocksize - (len(data) % blocksize);
    for i in range(numBytes):
        data += bytes(chr(numBytes), 'UTF-8');
    return data

def test9():
    input1 = b'Yellow Submarine'
    result1 = addPKCS7Padding(input1, 20);
    print(result1)


if __name__ == "__main__":
    test9()
        
    