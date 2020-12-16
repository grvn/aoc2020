#!/usr/bin/env python3
from sys import argv
from collections import defaultdict

def main():
  input = ([int(x) for x in open(argv[1]).read().split(',')])
  previous_seen = defaultdict(list,{key:[index] for index,key in enumerate(input,1)})
  n = input[-1]
  for i in range(len(input)+1, 30000001):
    if len(previous_seen[n]) == 1:
      n = 0
    else:
      n = previous_seen[n][-1] - previous_seen[n][-2]
    previous_seen[n].append(i)
  print(n)

if __name__ == '__main__':
  main()