#!/usr/bin/env python3

import sys
from random import random, choice

def mutate(dna, mutation_probability=0.4):
    mutate = mutation_probability / len(dna)  # scale chance to mutate by length of the sequence
    new_dna = ''
    bases = set('ACTG')
    for base in dna:
        if random() < mutate:
            new_base = choice(list(bases - set(base.upper())))  # choose a random base that is different to the current one
            if base.islower():
                new_base = new_base.lower()
        else:
            new_base = base
        new_dna += new_base
    return new_dna


if __name__ == '__main__':
    if len(sys.argv) == 2:
        dna = sys.argv[1]
    else:
        dna = 'GATACCA' * 6
    
    print(mutate(dna))
