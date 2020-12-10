#!/usr/bin/env python3
from sys import argv
from collections import Counter
from functools import lru_cache

@lru_cache(maxsize=None)
def nr_of_combinations(start, goal, adapters):
  if start == goal:
    return 1
  ret = 0
  for i in range(1,4):
    if (start + i) in adapters:
      ret += nr_of_combinations(start+i, goal, adapters)
  return ret

def main():
  with open(argv[1]) as f:
    input = sorted([int(line.strip()) for line in f])
  input = [0] + input + [input[-1] + 3]
  print("Total number of distinct ways:",nr_of_combinations(0, input[-1], tuple(input))) # konvertera till tuple så lru_cache kan användas

if __name__ == '__main__':
  main()