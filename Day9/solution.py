#!/bin/python3
import sys
import cProfile

PREAMBLE_LENGTH = 5


def main():
    f = open(sys.argv[1], "r")
    series = list(map(int, f.readlines()))
    f.close()

    input_length = len(series)

    a = 0
    b = 0
    s = 0
    n = 0
    next_number = 0
    for i in range(0, input_length - PREAMBLE_LENGTH):
        a = series[i]
        next_number = series[i + PREAMBLE_LENGTH]
        n = 1
        while n <= PREAMBLE_LENGTH:
            b = series[i + n]

            s = a + b
            # print(i, a, b, s, next_number)
            if s == next_number:
                print("")
                break
            n += 1
            if n == PREAMBLE_LENGTH:
                print(a, b, s)


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
