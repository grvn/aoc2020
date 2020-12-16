#!/usr/bin/env python3
from sys import argv
import re
from collections import defaultdict

regex_mem = re.compile("^mem\[(?P<address>\d+)\] = (?P<value>\d+)$")

def replace_first(the_list,value,replace):
  for i,x in enumerate(the_list):
    if x == value:
      the_list[i] = replace
      return the_list

def addresses(masked_address):
  if "X" in masked_address:
    return addresses(replace_first(masked_address.copy(),'X','0')) + addresses(replace_first(masked_address.copy(),'X','1'))
  else:
    return [masked_address]

def main():
  memory = defaultdict(int)
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  for line in input:
    if line.startswith("mask"):
      mask = line.split(' ')[2]
    elif line.startswith("mem"):
      search = regex_mem.match(line)
      address = search.group('address')
      address = list("%036d" % int(bin(int(address))[2:]))
      if "1" or "X" in mask:
        address = [mask[i] if mask[i] in "1X" else address[i] for i in range(36)]
      value = int(search.group('value'))
      for registry in addresses(address):
        memory[int("".join(registry),2)] = value
    else:
      raise ValueError('invalid input')
  print(sum(memory.values()))

if __name__ == '__main__':
  main()