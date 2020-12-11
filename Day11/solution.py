#!/bin/python3
import sys
import cProfile

FREE = "L"
OCCUPIED = "#"
FLOOR = "."


class Spot:
    def __init__(self, spotType, row, col):
        self.rowNbr = row
        self.colNbr = col
        self.isFloor = False
        if spotType == FLOOR:
            self.currentState = FLOOR
            self.nextState = FLOOR
            self.isFloor = True
        else:
            self.currentState = FREE
            self.nextState = OCCUPIED
            self.isFloor = False
        return


class Room:
    def __init__(self, seatMap):
        self.seatMap = []
        self.getSeatMap(seatMap)
        self.rowQty = len(self.seatMap[0])
        self.colQty = len(self.seatMap)
        self.show()
        return

    def getSeatMap(self, seatMap):
        seatRow = []
        row = 0
        col = 0
        for s in seatMap:
            for l in s:
                seatRow.append(Spot(l, row, col))
                row += 1
            self.seatMap.append(seatRow)
            seatRow = []
            row = 0
            col += 1
        return

    def show(self):
        for s in self.seatMap:
            for l in s:
                print(l.currentState, end="")
            print("")
        return

    def getAdjacent(self):
        return

    def populate(self):
        return


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str.strip, f.readlines()))
    f.close()

    room = Room(puzzle_input)


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
