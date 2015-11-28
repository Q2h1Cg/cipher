#!/usr/bin/env python
# Written against python 3.3.1
# Matasano Problem 21
# Implement the MT19937 Mersenne Twister RNG
# generated from code on the wikipedia

class MT19937:
    def __init__(self, seed):
        self.MT = [0] * 624;
        self.index = 0;
        self.seed = 0;
        self.initialize_generator(seed);

    def initialize_generator(self, seed):
        i = 0;
        self.MT[0] = seed;
        for i in range(1, 624):
            self.MT[i] = 0xffffffff & (0x6c078965 * (self.MT[i-1] ^ (self.MT[i-1] >> 30)) + i);
            
    def extract_number(self):
        if (self.index == 0):
            self.generate_numbers();
            
        y = self.MT[self.index];        
        y = y ^ (y >> 11);
        y = y ^ ((y << 7) & 0x9d2c5680);
        y = y ^ ((y << 15) & 0xefc60000);
        y = y ^ (y >> 18);
        
        self.index = (self.index+1)%624
        return y;
            
    def generate_numbers(self):
        for i in range(624):
            y = (self.MT[i] & 0x80000000) + (self.MT[(i+1)%624] & 0x7fffffff);
            self.MT[i] = self.MT[(i+397)%624] ^ (y >> 1);
            if ((y%2) != 0):
                self.MT[i] = self.MT[i] ^ 0x9908b0df;
        
if __name__ == "__main__":
    myMT = MT19937(12345);
    fail = False;
    for i in range(10):
        my = myMT.extract_number();
        print(hex(my));

