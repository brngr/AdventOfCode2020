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
        pos1 = int(tmp.pop().strip()) - 1
        pos2 = int(tmp.pop().strip()) - 1
        self.pos2 = pos2
        self.pos1 = pos1
        self.letter = letter
        self.password = password
        return

    def isValid(self):
        if (self.password[self.pos1] == self.letter) ^ (
            self.password[self.pos2] == self.letter
        ):
            return 1
        else:
            return 0


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