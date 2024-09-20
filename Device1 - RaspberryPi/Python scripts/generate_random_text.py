#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import loremipsum

MEGA_BYTE = 2**20
KILO_BYTE = 2**10

def genRndFile(filename, size):
    """Generate a random file of around a specific size in KB filled with lorem ipsum style text."""
    sizeBytes = size*KILO_BYTE # size in bytes

    text = ""
    while sys.getsizeof(text) < sizeBytes:
        sentence = loremipsum.generate_sentence(True)[2]
        text += sentence + " "

    file = open(filename, 'w')
    file.write(text)
    file.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print("genRndFile <filename> <size in KB>")
    else:
        filename = sys.argv[1]
        size = float(sys.argv[2])       # size in KB
        genRndFile(filename, size)
