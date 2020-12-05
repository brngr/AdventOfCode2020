#!/bin/python3
import sys
import cProfile
import re

RE_BYR = "byr:"
RE_IYR = "iyr:"
RE_EYR = "eyr:"
RE_HGT = "hgt:"
RE_HCL = "hcl:"
RE_ECL = "ecl:"
RE_PID = "pid:"
RE_CID = "cid:"
re_byr = re.compile(RE_BYR)
re_iyr = re.compile(RE_IYR)
re_eyr = re.compile(RE_EYR)
re_hcl = re.compile(RE_HGT)
re_hgt = re.compile(RE_HCL)
re_ecl = re.compile(RE_ECL)
re_pid = re.compile(RE_PID)
re_cid = re.compile(RE_CID)

# Part 2
# RE_BYR = "byr:\d{4}"
# RE_IYR = "iyr:\d{4}"
# RE_EYR = "eyr:\d{4}"
# RE_HGT = "hgt:"
# RE_HCL = "hcl:#[a-f0-9]{6}"
# RE_ECL = "ecl:[a-z]{3}"
# RE_PID = "pid:[0-9]{9}"
# RE_CID = "cid:"

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#    If cm, the number must be at least 150 and at most 193.
#    If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


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
        # if self.isValid:
        #    self.getData()
        #    # self.showData()
        #    self.isValid = self.checkValues()
        return

    def showData(self):
        print("byr: " + str(self.byr))
        print("iyr: " + str(self.iyr))
        print("eyr: " + str(self.eyr))
        print("hgt: " + str(self.hgt))
        print("hcl: " + str(self.hcl))
        print("ecl: " + str(self.ecl))
        print("pid: " + str(self.pid))
        print("")

    def checkValiditiy(self):
        if re_byr.search(self.data) is None:
            return False
        if re_iyr.search(self.data) is None:
            return False
        if re_eyr.search(self.data) is None:
            return False
        if re_hcl.search(self.data) is None:
            return False
        if re_hgt.search(self.data) is None:
            return False
        if re_ecl.search(self.data) is None:
            return False
        if re_pid.search(self.data) is None:
            return False
        return True

    def getData(self):
        return

    def getFieldData(self, field, dataLength):
        return

    def checkValues(self):
        return


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
