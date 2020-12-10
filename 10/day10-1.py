#!/usr/bin/env python3
from sys import argv
from collections import Counter

def main():
  with open(argv[1]) as f:
    input = sorted([int(line.strip()) for line in f])
  input = [0] + input + [input[-1] + 3] # lägger till väggen + enhetens inbyggda adapter
  counters = Counter({1:0,3:0})
  prev_nr = 0
  for number in input:
    counters[number - prev_nr] += 1
    prev_nr = number
  print(counters[1] * counters[3])

if __name__ == '__main__':
  main()