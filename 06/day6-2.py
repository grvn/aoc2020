#!/usr/bin/env python3
from sys import argv

def main():
  count = 0
  with open(argv[1]) as f:
    for lines in f.read().split('\n\n'):
      line = [list(item) for item in lines.splitlines()]
      count+=len(set(line[0]).intersection(*line))
  print(count)

if __name__ == '__main__':
  main()