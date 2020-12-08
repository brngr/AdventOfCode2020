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
        self.codeVariation = []
        self.getCodeVariation()
        self.runCodeVariation()

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

    def runCode(self, code):
        while self.isRunning:
            self.runOne(code[self.next])
            if self.next > len(code) - 1:
                self.isRunning = False
                print("Done! The accumulator value is")
                print(self.accumulator)
                return
            elif self.next in self.history:
                self.isRunning = False
                # print("Stuck in a loop... Abort!")
                # print("The last accumulator value is")
                # print(self.accumulator)
                return
            else:
                self.history.append(self.next)

    def runCodeVariation(self):
        for variation in self.codeVariation:
            self.next = 0
            self.accumulator = 0
            self.jump = 0
            self.isRunning = True
            self.history = []
            # print("\n")
            # print("Running variation:")
            # print(variation)
            self.runCode(variation)

    def getCodeVariation(self):
        print("")
        buffer1 = []
        buffer3 = []
        buffer2 = []
        for i in range(0, len(self.code)):

            if self.code[i][0] != "nop" and self.code[i][0] != "jmp":
                pass
            else:
                if len(self.code[0:i]) > 0:
                    buffer1 = self.code[0:i]
                if self.code[i][0] == "nop":
                    buffer2 = [["jmp", self.code[i][1]]]
                elif self.code[i][0] == "jmp":
                    buffer2 = [["nop", self.code[i][1]]]
                if len(self.code[i:]) > 0:
                    buffer3 = self.code[i + 1 :]
                self.codeVariation.append(buffer1 + buffer2 + buffer3)
                buffer1 = []
                buffer3 = []
                buffer2 = []


def main():
    f = open(sys.argv[1], "r")
    puzzle_input = list(map(str.strip, f.readlines()))
    f.close()

    hgc(puzzle_input)


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
