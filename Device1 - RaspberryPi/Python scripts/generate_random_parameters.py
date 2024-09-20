import sys
import argparse
import random

KILO_BYTE = 2**10

def genRecord(recordIndex, parameters):
    line = str(recordIndex)
    for p in range(1, parameters+1):
        line += " " + str(random.random())
    line += "\n"
    return line

def genRndSize(filename, parameters, size):
    """Generate a random file of around a specific size in KB filled with lorem ipsum style text."""
    sizeBytes = size*KILO_BYTE # size in bytes

    text = ""
    r = 1
    while sys.getsizeof(text) < sizeBytes:
        line = genRecord(r, parameters)
        text += line
        r += 1

    file = open(filename, 'w')
    file.write(text)
    file.close()

def genRndRecords(filename, parameters, records):
    lines = ""
    for r in range(1, records+1):
        line = genRecord(r, parameters)
        lines += line

    file = open(filename, 'w')
    file.write(lines)
    file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random file with the format of a log of parameters.")

    parser.add_argument('-f', dest='filename', metavar='file', default="file.txt", help='filename.')
    parser.add_argument('-p', dest='parameters', metavar='parameters', type=int, default=1, help='number of parameters.')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-r', dest='records', metavar='records', type=int, default=None, help='number of records.')
    group.add_argument('-s', dest='filesize', metavar='filesize', type=int, default=None, help='desired filesize in (KB).')

    args = parser.parse_args()
    filename = args.filename
    parameters = args.parameters
    records = args.records
    filesize = args.filesize

    if records is not None:
        genRndRecords(filename, parameters, records)

    if filesize is not None:
        genRndSize(filename, parameters, filesize)
