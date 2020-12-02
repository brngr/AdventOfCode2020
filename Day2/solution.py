#!/bin/python3
import sys
import cProfile


class Password:
    def __init__(self, line):
        tmp = line.split(": ")
        password = tmp.pop().strip()
        tmp = tmp[0].split(" ")
        letter = tmp.pop().strip()
        tmp = tmp[0].split("-")
        letter_max = int(tmp.pop().strip())
        letter_min = int(tmp.pop().strip())
        self.min = letter_min
        self.max = letter_max
        self.letter = letter
        self.password = password
        return

    def isValid(self):
        if (
            self.password.count(self.letter) < self.min
            or self.password.count(self.letter) > self.max
        ):
            return 0
        else:
            return 1


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str, f.readlines()))
    f.close()
    validPwCount = 0
    for p in puzzle_input:
        pw = Password(p)
        validPwCount += pw.isValid()
    print(validPwCount)
    return


if __name__ == "__main__":
    cProfile.run("main()")