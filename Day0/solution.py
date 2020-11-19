#!/bin/python3
import sys

def main():
    f = open(sys.argv[1],"r")
    input_file = list(map(int,f.readline().split(",")))
    f.close()
    return

if __name__ == "__main__":
    main()