#!/usr/bin/env python3

import sys

import evolve


if __name__ == '__main__':
    if len(sys.argv) == 2:
        rate = float(sys.argv[1])
    else:
        rate = 0.4
    base_sequence = "GGAATTGGTGACATGATTGAGGGGGCCGTTGAAGGGATTACTAAAAATGCATTGGTTCCC"
    for i in range(20):
        header = '>sample' + str(i+1) + '\n'
        sequence = evolve.mutate(base_sequence, rate)
        print(header + sequence)
