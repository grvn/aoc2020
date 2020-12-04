#!/usr/bin/env python3
from sys import argv

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

def main():
  valid=0
  req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
  with open(argv[1]) as f:
    input = f.read()
  for passport in input.split('\n\n'):
    fields = {k for k,_ in [x.strip().split(':') for x in passport.split()]}
    if req.issubset(fields):
      valid += 1
  print("Valid passports:",valid)

if __name__ == '__main__':
  main()