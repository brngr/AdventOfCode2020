#!/bin/python3
import sys
import cProfile


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str.strip, f.readlines()))
    f.close()

    print(puzzle_input)


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
