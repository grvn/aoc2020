#!/usr/bin/env python3
from sys import argv

# https://sv.wikipedia.org/wiki/Kinesiska_restklassatsen
# https://www.youtube.com/watch?v=1xKjh0mnDW4

def main():
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  buses = [(int(x),i) for i,x in enumerate(input[1].split(',')) if x != 'x']
  multiplier,answer = buses[0]
  for bus, offset in buses[1:]:
    while (answer + offset) % bus != 0:
      answer += multiplier
    multiplier *= bus
  print(answer)

if __name__ == '__main__':
  main()