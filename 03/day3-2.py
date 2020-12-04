#!/usr/bin/env python3
from sys import argv

def main():
  grid = []
  turns = [ (1,1), (3,1), (5,1), (7,1), (1,2) ]
  trees = 1
  with open(argv[1]) as f:
    for line in f:
      grid.append(list(x for x in line if x != '\n'))
  for turn in turns:
    trees *= count(turn[0],turn[1],grid)
  print("Multiplied trees:",trees)

def count(x_move,y_move, grid):
  trees = 0
  x,y = 0,0
  width = len(grid[0])
  height = len(grid)-1
  while y < height:
    x = (x+x_move) % width
    y += y_move
    if grid[y][x] == '#':
      trees += 1
  return trees

if __name__ == '__main__':
  main()