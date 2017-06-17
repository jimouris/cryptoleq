#!/usr/bin/python

from __future__ import print_function
import sys
import random

if len(sys.argv) != 3:
    print("Usage: python", sys.argv[0], "nums_to_generate max_bits_of_each_num")
    sys.exit()

for i in range(int(sys.argv[1])):
    print(random.getrandbits(int(sys.argv[2])), end=" ")
print(end="\n")
