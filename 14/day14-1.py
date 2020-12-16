#!/usr/bin/env python3
from sys import argv
import re
from collections import defaultdict

regex_mem = re.compile("^mem\[(?P<address>\d+)\] = (?P<value>\d+)$")

def main():
  memory = defaultdict(int)
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  for line in input:
    if line.startswith("mask"):
      mask = line.split(' ')[2]
    elif line.startswith("mem"):
      search = regex_mem.match(line)
      address = int(search.group('address'))
      value = "%036d" % int(bin(int(search.group('value')))[2:])
      memory[address] = int(''.join(value[i] if mask[i] == "X" else mask[i] for i in range(36)),2)
    else:
      raise ValueError('invalid input')
  print(sum(memory.values()))

if __name__ == '__main__':
  main()