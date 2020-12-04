#!/bin/python3
import sys
import cProfile
import re


class passport:
    def __init__(self, data):
        self.data = data
        self.isValid = self.checkValiditiy()
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
        if self.isValid:
            self.getData()
            self.showData()
        return

    def getFieldData(self, field, dataLength):
        fieldPos = self.data.find(field)
        if fieldPos != -1:
            if field != "hgt":
                value = self.data[
                    fieldPos + len(field) + 1 : fieldPos + len(field) + 1 + dataLength
                ]
                return value

            else:
                print("dgdfs")
                flag = True
                buffer = ""
                i = 0
                val = ""
                while flag:
                    val = self.data[fieldPos + len(field) + 1 + i]
                    buffer += val
                    if "cm" in buffer or "in" in buffer:
                        flag = False
                return buffer

        return

    def showData(self):
        print("byr: " + str(self.byr))
        print("iyr: " + str(self.iyr))
        print("eyr: " + str(self.eyr))
        print("hgt: " + str(self.hgt))
        print("hcl: " + str(self.hcl))
        print("ecl: " + str(self.ecl))
        print("pid: " + str(self.pid))

    def getData(self):
        self.byr = self.getFieldData("byr", 4)
        self.iyr = self.getFieldData("iyr", 4)
        self.eyr = self.getFieldData("eyr", 4)
        self.hgt = self.getFieldData("hgt", 0)
        self.hcl = self.getFieldData("hcl", 7)
        self.ecl = self.getFieldData("ecl", 3)
        self.pid = self.getFieldData("pid", 9)
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
        # if passportBuffer.isValid == True:
        #    count += 1
        # print(count)

    return


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
