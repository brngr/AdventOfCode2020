#!/bin/python3
import sys
import cProfile

def main():
    f = open(sys.argv[1],"r")
    #puzzle_input = list(map(int,f.readline().split(",")))
    #puzzle_input = list(map(int,f.readlines()))
    f.close()
    return

if __name__ == "__main__":
    cProfile.run('main()')