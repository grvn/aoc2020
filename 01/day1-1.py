#!/usr/bin/env python3
from sys import argv

def main():
  input = ([int(x) for x in open(argv[1]).readlines()])
  
  for x in input:
    for y in input:
      if x+y==2020:
        print('1:',x*y)
        exit()


if __name__ == '__main__':
  main()