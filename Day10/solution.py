#!/bin/python3
import sys
import cProfile


def main():
    f = open(sys.argv[1], "r")
    adapters = list(map(int, f.readlines()))
    f.close()

    inputRating = 0
    outputRating = 0

    oneJoltDiff = 0
    threeJoltsDiff = 1

    i = 0

    potential = 999

    while len(adapters) != 0:
        outputRating = adapters[i]
        if outputRating - inputRating <= 1:
            if potential > outputRating:
                potential = outputRating
        elif outputRating - inputRating <= 3:
            if potential > outputRating:
                potential = outputRating
        i += 1
        if i >= len(adapters):
            if potential - inputRating <= 1:
                oneJoltDiff += 1
            elif potential - inputRating <= 3:
                threeJoltsDiff += 1
            inputRating = adapters.pop(adapters.index(potential))
            potential = 999
            i = 0

    print(oneJoltDiff * threeJoltsDiff)


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
