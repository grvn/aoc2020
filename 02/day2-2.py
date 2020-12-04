#!/usr/bin/env python3
from sys import argv

def main():
  valid=0
  with open(argv[1]) as f:
    for line in f:
      a,b,passwd = line.strip().split()
      min,max = a.split('-')
      letter = b.strip(':')
      if (passwd[int(min)-1] == letter) ^ (passwd[int(max)-1] == letter):
        valid+=1
  print('1:',valid)

if __name__ == '__main__':
  main()