#!/bin/python3
import sys
import cProfile
import math


class boardingPass:
    def __init__(self, seat):
        self.seat = seat
        self.row = 0
        self.col = 0
        self.getRow()
        self.getCol()
        self.id = self.row * 8 + self.col
        return

    def getRow(self):
        lower = 0
        higher = 127
        for i in range(0, 7):
            if self.seat[i] == "F":
                lower = lower
                higher = math.floor((lower + higher) / 2)
                pass
            elif self.seat[i] == "B":
                lower = math.ceil((lower + higher) / 2)
                higher = higher
                pass
        self.row = lower
        return

    def getCol(self):
        lower = 0
        higher = 7
        for i in range(7, 10):
            if self.seat[i] == "L":
                lower = lower
                higher = math.floor((lower + higher) / 2)
                pass
            elif self.seat[i] == "R":
                lower = math.ceil((lower + higher) / 2)
                higher = higher
                pass
        self.col = higher
        return


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str.strip, f.readlines()))
    f.close()
    seats = []
    for p in puzzle_input:
        tmp = boardingPass(p)
        seats.append(tmp.id)

    seats.sort()
    for s in seats:
        if s + 1 not in seats and s + 2 in seats:
            print(s + 1)
    return


if __name__ == "__main__":
    cProfile.run("main()")
