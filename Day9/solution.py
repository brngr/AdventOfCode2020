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


def sumList(values):
    buffer = 0
    for h in range(0, len(values)):
        buffer += values[h]
    return buffer


def findSummingRange(invalid, values):
    a = 0
    for i in range(0, len(values)):
        for j in range(i, len(values)):
            a = sumList(values[i : j + 1])
            if a == invalid:
                return values[i : j + 1]
            if a > invalid:
                continue
    return None


def main():
    f = open(sys.argv[1], "r")

    series = list(map(int, f.readlines()))
    f.close()

    input_length = len(series)
    weakness = 0
    goal = 0
    for i in range(PREAMBLE_LENGTH, input_length):
        goal = series[i]
        invalid = findSum(goal, series[i - PREAMBLE_LENGTH : i])
        if invalid != 0:
            break

    summingRange = findSummingRange(invalid, series)
    weakness = min(summingRange) + max(summingRange)
    print(weakness)
    return


if __name__ == "__main__":
    # main()
    cProfile.run("main()")
