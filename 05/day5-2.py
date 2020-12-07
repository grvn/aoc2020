#!/usr/bin/env python3
from sys import argv

def main():
  seats = set(range(1024))
  with open(argv[1]) as f:
    for line in f:
      line = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
      seats.discard(int(line, 2))
    for seat in seats:
      if seat-1 not in seats and seat+1 not in seats:
        print("Your seat is:",seat)

if __name__ == '__main__':
  main()