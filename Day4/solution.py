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
            # self.showData()
            self.isValid = self.checkValues()
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
                flag = True
                buffer = ""
                i = 0
                val = ""
                while flag:
                    # print(self.data)
                    # print(fieldPos)
                    # print(buffer)
                    buffer += self.data[fieldPos + len(field) + 1 + i]
                    i += 1
                    if "cm" in buffer or "in" in buffer:
                        flag = False
                    if (
                        len(buffer) > 5
                        or fieldPos + len(field) + 1 + i > len(self.data) - 1
                    ):
                        return "00cm"
                return buffer
        return

    def checkValues(self):
        print(self.data)
        print("byr")
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if self.byr < 1920 or self.byr > 2002:
            return False
        print("iyr")
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if self.iyr < 2010 or self.iyr > 2020:
            return False
        print("eyr")
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if self.eyr < 2020 or self.eyr > 2030:
            return False
        print("hgt")
        # hgt (Height) - a number followed by either cm or in:
        #
        #    If cm, the number must be at least 150 and at most 193.
        #    If in, the number must be at least 59 and at most 76.
        unit = self.hgt[len(self.hgt) - 2] + self.hgt[len(self.hgt) - 1]
        height = int(self.hgt[0 : len(self.hgt) - 2])
        print(height)
        if unit == "cm":
            if height < 150 or height > 193:
                return False
        elif unit == "in":
            if height < 59 or height > 76:
                return False
        print("hcl")
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if len(self.hcl) == 7:
            if self.hcl[0] == "#":
                for l in self.hcl[1:7]:
                    if l not in [
                        "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9",
                        "a",
                        "b",
                        "c",
                        "d",
                        "e",
                        "f",
                    ]:
                        return False
            else:
                return False
        else:
            return False
        print("ecl")
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        print("pid")
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if len(self.pid) == 9:
            for a in self.pid:
                if int(a) not in range(0, 10):
                    return False
        else:
            return False

        return True

    def showData(self):
        print("byr: " + str(self.byr))
        print("iyr: " + str(self.iyr))
        print("eyr: " + str(self.eyr))
        print("hgt: " + str(self.hgt))
        print("hcl: " + str(self.hcl))
        print("ecl: " + str(self.ecl))
        print("pid: " + str(self.pid))
        print("")

    def getData(self):
        self.byr = int(self.getFieldData("byr", 4))
        self.iyr = int(self.getFieldData("iyr", 4))
        self.eyr = int(self.getFieldData("eyr", 4))
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
        if passportBuffer.isValid == True:
            count += 1
    print(count)

    return


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
