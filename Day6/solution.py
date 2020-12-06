#!/bin/python3
import sys
import cProfile


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str.strip, f.readlines()))
    f.close()
    puzzle_input.append("")

    answers = []
    tmp = ""
    for p in puzzle_input:
        if p != "":
            # print(p)
            for a in p:
                # print(a)
                if a not in tmp:
                    tmp = tmp + a
        else:
            answers.append(tmp)
            tmp = ""

    count = 0
    for a in answers:
        count += len(a)
    print(count)


if __name__ == "__main__":
    # cProfile.run("main()")
    main()