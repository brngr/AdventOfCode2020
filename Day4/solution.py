#!/bin/python3
import sys
import cProfile
import re


RE_BYR = "byr:\d{4} "
RE_IYR = "iyr:\d{4} "
RE_EYR = "eyr:\d{4} "
RE_HGT = "hgt:\d{2,}(cm|in) "
RE_HCL = "hcl:#[a-f0-9]{6}"
RE_ECL = "ecl:[a-z]{3} "
RE_PID = "pid:[0-9]{9} "
# RE_CID = "cid:"

re_byr = re.compile(RE_BYR)
re_iyr = re.compile(RE_IYR)
re_eyr = re.compile(RE_EYR)
re_hcl = re.compile(RE_HGT)
re_hgt = re.compile(RE_HCL)
re_ecl = re.compile(RE_ECL)
re_pid = re.compile(RE_PID)
# re_cid = re.compile(RE_CID)


class passport:
    def __init__(self, data):
        self.data = data
        self.isValid = False
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
        if self.getData() == True:
            self.isValid = self.checkValues()
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

    def getData(self):
        tmp = re_byr.search(self.data)
        if tmp != None:
            self.byr = int(
                self.data[tmp.span()[0] : tmp.span()[1]].split(":")[1].strip()
            )
        tmp = re_iyr.search(self.data)
        if tmp != None:
            self.iyr = int(
                self.data[tmp.span()[0] : tmp.span()[1]].split(":")[1].strip()
            )
        tmp = re_eyr.search(self.data)
        if tmp != None:
            self.eyr = int(
                self.data[tmp.span()[0] : tmp.span()[1]].split(":")[1].strip()
            )
        tmp = re_hcl.search(self.data)
        if tmp != None:
            self.hgt = self.data[tmp.span()[0] : tmp.span()[1]].split(":")[1].strip()
        tmp = re_hgt.search(self.data)
        if tmp != None:
            self.hcl = self.data[tmp.span()[0] : tmp.span()[1]].split(":")[1].strip()
        tmp = re_ecl.search(self.data)
        if tmp != None:
            self.ecl = self.data[tmp.span()[0] : tmp.span()[1]].split(":")[1].strip()
        tmp = re_pid.search(self.data)
        if tmp != None:
            self.pid = self.data[tmp.span()[0] : tmp.span()[1]].split(":")[1]
        return True

    def checkValues(self):
        if self.byr is None or self.byr not in range(1920, 2003):
            return False
        if self.iyr is None or self.iyr not in range(2010, 2021):
            return False
        if self.eyr is None or self.eyr not in range(2020, 2031):
            return False
        if self.hgt is not None:
            value = int(self.hgt[0 : len(self.hgt) - 2])
            unit = self.hgt[len(self.hgt) - 2 : len(self.hgt)]
            if unit == "cm":
                if value not in range(150, 194):
                    return False
            elif unit == "in":
                if value not in range(59, 77):
                    return False
        else:
            return False
        if self.hcl is None:
            return False
        if self.ecl is None or self.ecl not in [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        ]:
            return False
        if self.pid is None or self.pid is None:
            return False
        return True


def main():
    stringBuffer = ""
    f = open(sys.argv[1], "r")
    batchFile = list(map(str, f.readlines()))
    f.close()
    passportData = []

    for i in range(len(batchFile)):
        if batchFile[i] == "\n":
            passportData.append(stringBuffer.strip() + " ")
            stringBuffer = ""
        elif i == len(batchFile) - 1:
            stringBuffer += batchFile[i].replace("\n", " ")
            passportData.append(stringBuffer.strip() + " ")
            stringBuffer = ""
        else:
            stringBuffer += batchFile[i].replace("\n", " ")

    count = 0

    for p in passportData:
        passportBuffer = passport(p)
        if passportBuffer.isValid == True:
            count += 1
    print(count)

    return


if __name__ == "__main__":
    # main()
    cProfile.run("main()")
