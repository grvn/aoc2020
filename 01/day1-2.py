#!/usr/bin/env python3
from sys import argv

def main():
  input = ([int(x) for x in open(argv[1]).readlines()])
  
  for x in input:
    for y in input:
      for z in input:
        if x+y+z==2020:
          print('2:',x*y*z)
          exit()


if __name__ == '__main__':
  main()