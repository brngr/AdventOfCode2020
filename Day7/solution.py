#!/bin/python3
import sys
import re
import cProfile


class ProcessingRule:
    def __init__(self, rule):
        self.isCounted = False
        self.hasGold = False
        self.mainColor = rule.split(" bags contain ")[0]
        self.containedColor = rule.split(" bags contain ")[1]
        self.containedColor = re.sub(
            "[^a-zA-Z ]", "", self.containedColor
        )  # remove number and dot
        self.containedColor = re.split(
            " bags| bag", self.containedColor
        )  # split by bag color
        for i in range(
            0, len(self.containedColor)
        ):  # remove trailing space and empty strings
            self.containedColor[i] = self.containedColor[i].strip()
            if self.containedColor[i] == "":
                self.containedColor.pop(i)
        for color in self.containedColor:
            if color == "shiny gold":
                self.hasGold = True


def main():
    f = open(sys.argv[1], "r")
    # f = open("/home/bere/AoC/AdventOfCode2020/Day7/test1", "r")
    puzzle_input = list(map(str.strip, f.readlines()))
    f.close()
    count = 0
    prevCount = 0
    rules = []
    for p in puzzle_input:
        rules.append(ProcessingRule(p))

    containgGold = []
    for r in rules:
        if r.hasGold:
            r.isCounted = True
            containgGold.append(r.mainColor)
            count += 1
    while prevCount != count:
        prevCount = count
        for r in rules:
            for c in r.containedColor:
                if c in containgGold and r.isCounted == False:
                    count += 1
                    r.isCounted = True
                    containgGold.append(r.mainColor)

    print(count)


if __name__ == "__main__":
    # cProfile.run("main()")
    main()
