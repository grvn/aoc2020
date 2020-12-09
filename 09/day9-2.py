#!/usr/bin/env python3
from sys import argv
from itertools import combinations
from collections import deque

def find_fault(input: list, preamble_size: int):
  preamble = deque(input[:preamble_size][::-1])
  values = input[preamble_size:]
  for value in values:
    done = True
    for x,y in combinations(preamble,2):
      if x+y==value:
        done = False
        break
    if done:
      return value
    preamble.appendleft(value)
    preamble.pop()

def main():
  preamble_size = int(argv[2])
  with open(argv[1]) as f:
    input = [int(line.strip()) for line in f]
  fault = find_fault(input,preamble_size)
  for i in range(len(input)):
    total = input[i]
    end = i+1
    while total < fault:
      total += input[end]
      end += 1
    if total == fault:
      r = input[i:end]
      print("Encryption weakness:",min(r) + max(r))
      exit()


if __name__ == '__main__':
  main()