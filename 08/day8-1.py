#!/usr/bin/env python3
from sys import argv

def acc(pc,acc,value): return pc+1,acc+value
def jmp(pc,acc,value): return pc+value,acc
def nop(pc,acc,value): return pc+1,acc

functions={'acc':acc,'jmp':jmp,'nop':nop}

def main():
  accumulator = 0
  pc = 0
  used = set()
  with open(argv[1]) as f:
    instructions = [(x,int(y)) for x,y in [line.strip().split(" ") for line in f]]
  while pc not in used:
    used.add(pc)
    instruction = instructions[pc]
    try:
      pc,accumulator = eval(instruction[0],{'__builtins__':None},functions)(pc,accumulator,instruction[1])
    except KeyError:
      raise ValueError('invalid input')
  print("Accumulator has the value:",accumulator)

if __name__ == '__main__':
  main()