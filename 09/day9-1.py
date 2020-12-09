#!/usr/bin/env python3
from sys import argv
from itertools import combinations
from collections import deque

def main():
  preamble_size = int(argv[2])
  with open(argv[1]) as f:
    input = [int(line.strip())for line in f]
  preamble = deque(input[:preamble_size][::-1])
  values = input[preamble_size:]
  for value in values:
    done = True
    for x,y in combinations(preamble,2):
      if x+y==value:
        done = False
        break
    if done:
      print(value)
      exit()
    preamble.appendleft(value)
    preamble.pop()

if __name__ == '__main__':
  main()