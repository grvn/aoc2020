#!/usr/bin/env python3
from sys import argv

rows = -1
columns = -1

def adjacent(x,y,grid):
  for (yy,xx) in [(-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1),(+1,-1),(+1,0),(+1,+1)]:
    yield find_next(x,y,yy,xx,grid)

def find_next(x,y,off_y,off_x,grid):
  x += off_x
  y += off_y
  n = 1
  while y >= 0 and x >= 0 and y < rows and x < columns:
    if grid[y][x] != '.':
      return grid[y][x]
    x += off_x
    y += off_y
    n += 1
  return '.'

def round(grid):
  new_grid = []
  for y,row in enumerate(grid):
    column = []
    for x, seat in enumerate(row):
      if seat == 'L' and tuple(adjacent(x,y,grid)).count('#') == 0:
          column.append('#')
          continue
      if seat == '#' and tuple(adjacent(x,y,grid)).count('#') >= 5:
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