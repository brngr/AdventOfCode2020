#!/bin/python3
import sys
import cProfile

PREAMBLE_LENGTH = 25


def findSum(goal, values):
    a = 0
    b = 0
    c = 0
    for i in range(0, len(values)):
        a = values[i]
        for j in range(i + 1, len(values)):
            b = values[j]
            c = a + b
            if c == goal:
                return 0
    return goal


def main():
    f = open(sys.argv[1], "r")
    series = list(map(int, f.readlines()))
    f.close()

    input_length = len(series)

    goal = 0
    for i in range(PREAMBLE_LENGTH, input_length):
        goal = series[i]
        if findSum(goal, series[i - PREAMBLE_LENGTH : i]) != 0:
            print(goal)
            break
    return


if __name__ == "__main__":
    # main()
    cProfile.run("main()")
