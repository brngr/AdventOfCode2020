#!/bin/python3
import sys
import cProfile


class passport:
    def __init__(self, data):
        self.data = data
        self.isValid = self.checkValiditiy()
        return

    def checkValiditiy(self):
        # rewrite with regex
        if "byr:" not in self.data:
            return False
        if "iyr:" not in self.data:
            return False
        if "eyr:" not in self.data:
            return False
        if "hgt:" not in self.data:
            return False
        if "hcl:" not in self.data:
            return False
        if "ecl:" not in self.data:
            return False
        if "pid:" not in self.data:
            return False
        # if "cid" not in self.data:
        #    return False
        return True


def main():
    stringBuffer = ""
    f = open(sys.argv[1], "r")
    batchFile = list(map(str, f.readlines()))
    f.close()
    passportData = []
    # print(batchFile)
    for i in range(len(batchFile)):
        if batchFile[i] == "\n":
            passportData.append(stringBuffer.strip())
            stringBuffer = ""
        elif i == len(batchFile) - 1:
            stringBuffer += batchFile[i].replace("\n", " ")
            passportData.append(stringBuffer.strip())
            stringBuffer = ""
        else:
            stringBuffer += batchFile[i].replace("\n", " ")

    count = 0
    # print(passportData)
    for p in passportData:
        passportBuffer = passport(p)
        # print(passportBuffer.data)
        if passportBuffer.isValid == True:
            count += 1
    print(count)
    return


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
