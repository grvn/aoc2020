#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from itertools import product

def get_neighbors(pos):
  return [x for x in list(product(*[range(p-1, p+2) for p in pos])) if x != pos]

def main():
  input = defaultdict(int)
  next = defaultdict(int)
  with open(argv[1]) as f:
    for y,line in enumerate([line.strip() for line in f]):
      for x, char in enumerate(line):
        input[(x,y,0)] = char

  for _ in range(6):
    for k in input.keys():
      for n_k in get_neighbors(k):
        next[n_k] = '.'
    for k in next.keys():
      if input[k] == '#':
        if list(map(input.get, get_neighbors(k))).count('#') in (2,3):
          next[k] = '#'
        else:
          next[k] = '.'
      else:
        if list(map(input.get, get_neighbors(k))).count('#') == 3:
          next[k] = '#'
        else:
          next[k] = '.'
    input = next.copy()
  print(sum(map(('#').__eq__, next.values())))

if __name__ == '__main__':
  main()