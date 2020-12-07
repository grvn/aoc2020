#!/usr/bin/env python3
from sys import argv

def main():
  count = 0
  with open(argv[1]) as f:
    for line in f.read().split('\n\n'):
      count+=len(set(line.replace('\n','')))
  print(count)


if __name__ == '__main__':
  main()