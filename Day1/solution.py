#!/bin/python3
import sys

def main():
    f = open(sys.argv[1],"r")
    puzzle_input = list(map(int,f.readlines()))
    f.close()

    for i in puzzle_input:
        for j in puzzle_input:
            if i + j == 2020:
                print(i*j)
                return

if __name__ == "__main__":
    main()