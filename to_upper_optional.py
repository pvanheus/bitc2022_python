#!/usr/bin/env python3

import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=argparse.FileType())
    parser.add_argument('output_file', type=argparse.FileType('w'), nargs='?', default=sys.stderr)
    args = parser.parse_args()

    for line in args.input_file:
        output_line = line.upper()
        args.output_file.write(output_line)

        