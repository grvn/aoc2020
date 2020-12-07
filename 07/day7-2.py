#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
import re
import itertools

regex_pattern = re.compile('^(?P<bag>[a-z ]*) bags contain (?P<content>.*)$')
regex_bags = re.compile('^[, ]?(\d+) ([a-z ]*) bag[s,.]*$')
contains = defaultdict(list)

def main():
  with open(argv[1]) as f:
    for line in f:
      search = regex_pattern.match(line)
      parents = [regex_bags.findall(bag) for bag in search.group('content').split(',')]
      for bag in itertools.chain.from_iterable(parents):
        contains[search.group('bag')].append(bag)
  print("shiny gold contains:",find_bags((1,'shiny gold'))-1,"other bags")

def find_bags(item):
  content = contains[item[1]]
  tmp = 1
  for next in content:
    tmp += find_bags(next)
  return int(item[0]) * tmp


if __name__ == '__main__':
  main()