#!/usr/bin/env python3
from sys import argv

def main():
  maximum = 0
  with open(argv[1]) as f:
    for line in f:
      line = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
      maximum = max(maximum, int(line, 2))
  print("Highest seat ID:",maximum)

if __name__ == '__main__':
  main()