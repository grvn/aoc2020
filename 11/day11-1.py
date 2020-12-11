#!/usr/bin/env python3
from sys import argv

rows = -1
columns = -1

def adjacent(x,y,grid):
  for yy in range (y-1, y+2):
    for xx in range (x-1,x+2):
      if (yy,xx)!=(y,x) and yy >= 0 and xx >= 0 and yy < rows and xx < columns:
        yield grid[yy][xx]

def round(grid):
  new_grid = []
  for y,row in enumerate(grid):
    column = []
    for x, seat in enumerate(row):
      if seat == 'L':
        if tuple(adjacent(x,y,grid)).count('#') == 0:
          column.append('#')
          continue
      if seat == '#':
        if tuple(adjacent(x,y,grid)).count('#') >= 4:
          column.append('L')
          continue
      column.append(seat)
    new_grid.append(column)
  return new_grid

def main():
  global rows
  global columns
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  grid = list(map(list, input))
  rows = len(grid)
  columns = len(grid[0])
  prev = []
  while grid != prev:
    prev = grid
    grid = round(grid)
  print("Occupied seats:",sum([row.count("#") for row in grid]))

if __name__ == '__main__':
  main()