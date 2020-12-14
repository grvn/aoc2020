#!/usr/bin/env python3
from sys import argv

def main():
  x,y = 0,0
  directions = ('E','S','W','N')
  direction = 0
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  for line in input:
    dir = line[0]
    dist = int(line[1:])
    if dir == 'N':
      y -= dist
    elif dir == 'S':
      y += dist
    elif dir == 'E':
      x += dist
    elif dir == 'W':
      x -= dist
    elif dir == 'L':
      direction = (direction - (dist // 90)) % 4
    elif dir == 'R':
      direction = (direction + (dist // 90)) % 4
    elif dir == 'F':
      if directions[direction] == 'N':
        y -= dist
      elif directions[direction] == 'S':
        y += dist
      elif directions[direction] == 'E':
        x += dist
      elif directions[direction] == 'W':
        x -= dist
  print(abs(x) + abs(y))


if __name__ == '__main__':
  main()