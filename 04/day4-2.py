#!/usr/bin/env python3
from sys import argv
import re

"""\
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

def main():
  valid=0
  req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
  eye_color = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
  with open(argv[1]) as f:
    input = f.read()
  for passport in input.split('\n\n'):
    fields = {k:v for k,v in [x.strip().split(':') for x in passport.split()]}
    if (req.issubset(fields) and 
        fields['ecl'] in eye_color):
      if (1920 <= int(fields['byr']) <= 2002 and 
          2010 <= int(fields['iyr']) <= 2020 and 
          2020 <= int(fields['eyr']) <= 2030):
        if (re.match('^#[a-f0-9]{6}$', fields['hcl']) and 
            re.match('^[0-9]{9}$', fields['pid'])):
          search = re.match('^(?P<height>\d+)(?P<unit>cm|in)$', fields['hgt'])
          if search:
            if (search.group('unit') == 'cm' and 150 <= int(search.group('height')) <= 193 or 
                search.group('unit') == 'in' and 59 <= int(search.group('height')) <= 76):
              valid+=1
  print("Valid passports:",valid)

if __name__ == '__main__':
  main()