#!/bin/python3
import sys


def main():
    f = open(sys.argv[1],"r")
    puzzle_input = list(map(int,f.readlines()))
    f.close()
    for i in puzzle_input:
        tmp1 = 2020 - i
        for l in puzzle_input:
            tmp2 = tmp1 - l
            if tmp2 in puzzle_input:
                print(i*l*tmp2)
                return

if __name__ == "__main__":
    main()