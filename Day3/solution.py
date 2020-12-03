#!/bin/python3
import sys
import cProfile


class Grid:
    def __init__(self, pattern, slop):
        self.pattern = pattern
        self.grid = []
        self.posX = 0
        self.posY = 0
        self.bottom = len(pattern) - 1
        self.count = 0
        self.TREE = "#"
        self.DOT = "."
        self.right = slop[0]
        self.down = slop[1]

    def show(self):
        print(self.grid)

    def grow(self):
        if len(self.grid) == 0:
            for i in range(0, len(self.pattern)):
                self.grid.append(self.pattern[i])
            return
        for i in range(0, len(self.pattern)):
            self.grid[i] += self.pattern[i]
        return

    def isTree(self, point):
        if point == self.TREE:
            return True
        if point == self.DOT:
            return False

    def checkSizeX(self):
        if self.posX + self.right > len(self.grid[0]) - 1:
            return False
        else:
            return True

    def checkSizeY(self):
        if self.posY < self.bottom:
            return True
        else:
            return False

    def moveOnGrid(self):
        self.posX = self.posX + self.right
        self.posY = self.posY + self.down
        return

    def runTrajectory(self):
        self.grow()
        while self.checkSizeY():
            if self.checkSizeX() == False:
                self.grow()
            self.moveOnGrid()

            if self.isTree(self.grid[self.posY][self.posX]):
                self.count += 1
        return self.count


def main():
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    answer = 1
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str, f.readlines()))
    f.close()

    for i in range(len(puzzle_input)):
        puzzle_input[i] = puzzle_input[i].strip()

    for s in slopes:
        grid = Grid(puzzle_input, s)
        answer = answer * grid.runTrajectory()
    print(answer)
    return


if __name__ == "__main__":
    cProfile.run("main()")