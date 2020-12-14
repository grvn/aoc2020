#!/usr/bin/env python3
from sys import argv

def main():
  x,y = 0,0
  wx,wy = 10,1
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  for line in input:
    dir = line[0]
    dist = int(line[1:])
    if dir == 'N':
      wy += dist
    elif dir == 'S':
      wy -= dist
    elif dir == 'E':
      wx += dist
    elif dir == 'W':
      wx -= dist
    elif dir == 'L':
      for i in range((dist//90)%4):
        wx,wy = wy,wx
        wx *= -1
    elif dir == 'R':
      for i in range((dist//90)%4):
        wx,wy = wy,wx
        wy *= -1
    elif dir == 'F':
      x += dist * wx
      y += dist * wy
  print(abs(x) + abs(y))

if __name__ == '__main__':
  main()