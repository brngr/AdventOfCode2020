#!/bin/python3
import sys
import cProfile


class hgc:
    def __init__(self, bootCode):
        self.code = []
        for bc in bootCode:
            buffer = bc.split(" ")
            self.code.append([buffer[0], int(buffer[1])])
        self.next = 0
        self.accumulator = 0
        self.jump = 0
        self.isRunning = True
        self.history = []
        self.runCode()

    def nop(self):
        self.jump = 1
        return

    def acc(self, value):
        self.accumulator += value
        self.jump = 1
        return

    def jmp(self, offset):
        self.jump = offset
        return

    def runOne(self, codeLine):
        operation = codeLine[0]
        value = codeLine[1]
        if operation == "nop":
            self.nop()
        elif operation == "acc":
            self.acc(value)
        elif operation == "jmp":
            self.jmp(value)
        self.next += self.jump
        self.jump = 0
        return

    def runCode(self):
        while self.isRunning:
            self.runOne(self.code[self.next])
            if self.next in self.history:
                self.isRunning = False
            else:
                self.history.append(self.next)
        print(self.accumulator)


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str.strip, f.readlines()))
    f.close()

    hgc(puzzle_input)


if __name__ == "__main__":
    # main()
    cProfile.run("main()")
