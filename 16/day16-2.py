#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from itertools import chain
import re
from functools import reduce

regex_rule = re.compile("^(?P<name>[^:]+): (?P<min_r1>\d+)-(?P<max_r1>\d+) or (?P<min_r2>\d+)-(?P<max_r2>\d+)$")

def find_valid_tickets(tickets, valid):
  for ticket in tickets:
    values = [int(i) for i in ticket.split(',')]
    invalid = [item for item in values if item not in valid]
    if len(invalid) == 0:
      yield values

def main():
  fields, my_ticket, nearby_tickets = open(argv[1]).read().split('\n\n')
  my_ticket = [int(i) for i in my_ticket.splitlines()[1].split(',')]
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
  valid_tickets = list(find_valid_tickets(nearby_tickets.splitlines()[1:], valid))
  possible_positions = defaultdict(dict)
  for pos in range(len(valid_tickets[0])):
    possible_positions[pos] = {name for name, valid_values in rules.items() if all(ticket[pos] in valid_values for ticket in valid_tickets)}  
  positions = {}
  while len(possible_positions) != 0:
    for key, values in list(possible_positions.items()):
      if len(values) == 1:
        locked_key = values.pop()
        positions[locked_key] = key
        possible_positions.pop(key)
        for dict_values in possible_positions.values():
          dict_values.discard(locked_key)
  departure_values = [my_ticket[pos] for key, pos in positions.items() if key.startswith('departure')]
  answer = reduce((lambda x,y: x*y), departure_values)
  print(answer)


if __name__ == '__main__':
  main()