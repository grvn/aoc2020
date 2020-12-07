#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
import re
import itertools

regex_pattern = re.compile('^(?P<bag>[a-z ]*) bags contain (?P<content>.*)$')
regex_bags = re.compile('^[, ]?\d+ ([a-z ]*) bag[s,.]*$')
contains = defaultdict(list)
colors = set()

def main():
  with open(argv[1]) as f:
    for line in f:
      search = regex_pattern.match(line)
      # if(search.group('content') != "no other bags."):
      parents = [regex_bags.findall(bag) for bag in search.group('content').split(',')]
      for bag in itertools.chain.from_iterable(parents):
        contains[bag].append(search.group('bag'))
  find_parents('shiny gold')
  print("Number of colors:",len(colors))

def find_parents(child):
  children = contains[child]
  for kid in children:
    if kid not in colors:
      colors.add(kid)
      find_parents(kid)

if __name__ == '__main__':
  main()