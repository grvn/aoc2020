#!/usr/bin/env python3
from sys import argv

def main():
  grid = []
  trees = 0
  x,y = 0,0
  with open(argv[1]) as f:
    for line in f:
      grid.append(list(x for x in line if x != '\n'))

  width = len(grid[0])
  height = len(grid)-1

  while y < height:
    x = (x+3) % width
    y += 1
    if grid[y][x] == '#':
      trees += 1

  print("Trees:",trees)

if __name__ == '__main__':
  main()