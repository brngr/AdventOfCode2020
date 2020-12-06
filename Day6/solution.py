#!/bin/python3
import sys
import cProfile


def main():
    f = open(sys.argv[1], "r")

    puzzle_input = list(map(str.strip, f.readlines()))

    f.close()
    puzzle_input.append("")

    group = []
    answers = []

    for p in puzzle_input:
        if p != "":
            group.append(p)
        else:
            answered = group[0]
            if len(group) > 1:
                for a in answered:
                    for i in range(1, len(group)):
                        if a not in group[i]:
                            answered = answered.replace(a, "")
            answers.append(answered)
            group = []
            pass

    count = 0
    for a in answers:
        count += len(a)
    print(count)


if __name__ == "__main__":
    # cProfile.run("main()")
    main()