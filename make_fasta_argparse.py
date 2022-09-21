#!/usr/bin/env python3

import argparse

import evolve


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rate', type=float, default=0.4)
    parser.add_argument('-n', '--num_sequences', type=int, default=20)
    parser.add_argument('--dna', default="GGAATTGGTGACATGATTGAGGGGGCCGTTGAAGGGATTACTAAAAATGCATTGGTTCCC")
    args = parser.parse_args()

    base_sequence = args.dna
    for i in range(args.num_sequences):
        header = '>sample' + str(i+1) + '\n'
        sequence = evolve.mutate(base_sequence, args.rate)
        print(header + sequence)
