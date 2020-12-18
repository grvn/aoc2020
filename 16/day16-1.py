#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from itertools import chain
import re

regex_rule = re.compile("^(?P<name>[^:]+): (?P<min_r1>\d+)-(?P<max_r1>\d+) or (?P<min_r2>\d+)-(?P<max_r2>\d+)$")

def main():
  fields, _, nearby_tickets = open(argv[1]).read().split('\n\n')
  rules = defaultdict(set)
  for field in fields.splitlines():
    search = regex_rule.match(field)
    valid = set(
      chain(
        range(int(search.group('min_r1')),int(search.group('max_r1'))+1), 
        range(int(search.group('min_r2')),int(search.group('max_r2'))+1)
        )
      )
    rules[search.group('name')] = valid
  valid = set().union(*rules.values())
  ticket_values = list(chain.from_iterable(([int(i) for i in ticket.split(',')] for ticket in nearby_tickets.splitlines()[1:])))
  invalid = [item for item in ticket_values if item not in valid]
  print(sum(invalid))

if __name__ == '__main__':
  main()