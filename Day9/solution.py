#!/bin/python3
import sys
import cProfile

PREAMBLE_LENGTH = 5


def findSum(goal, values):
    print(goal, values)
    return


def main():
    f = open(sys.argv[1], "r")
    series = list(map(int, f.readlines()))
    f.close()

    input_length = len(series)

    goal = 0
    for i in range(5, input_length):
        goal = series[i]
        findSum(goal, series[i - PREAMBLE_LENGTH : i])


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
