#!/usr/bin/env python3
from sys import argv
from math import inf

def main():
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  earliest = int(input[0])
  buses = [int(x) for x in input[1].split(',') if x != 'x']
  bus_id = None
  departure = inf
  for bus in buses: 
    close = (earliest//bus)*bus
    if close < earliest:
      close += bus
    if close < departure:
      bus_id = bus
      departure = close
  print(bus_id * (departure - earliest))


if __name__ == '__main__':
  main()