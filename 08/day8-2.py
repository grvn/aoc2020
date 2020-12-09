#!/usr/bin/env python3
from sys import argv

def acc(pc,acc,value): return pc+1,acc+value
def jmp(pc,acc,value): return pc+value,acc
def nop(pc,acc,value): return pc+1,acc

functions={'acc':acc,'jmp':jmp,'nop':nop}

def run(instructions):
  accumulator = 0
  pc = 0
  used = set()
  code_size = len(instructions)
  while pc not in used and pc < code_size:
    used.add(pc)
    instruction = instructions[pc]
    try:
      pc,accumulator = eval(instruction[0],{'__builtins__':None},functions)(pc,accumulator,instruction[1])
    except KeyError:
      raise ValueError('invalid input')
  if pc >= code_size:
    return accumulator
  else:
    raise RuntimeError(used)
  
def main():
  with open(argv[1]) as f:
    instructions = [(x,int(y)) for x,y in [line.strip().split(" ") for line in f]]
  try:
    run(instructions)
  except RuntimeError as e:
    possibles, = e.args
  for possible in possibles:
    if instructions[possible][0] in ('nop','jmp') and instructions[possible][1] != 0:
      test_instruction = instructions.copy()
      test_instruction[possible] = ('nop',instructions[possible][1]) if instructions[possible][0] == 'jmp' else ('jmp',instructions[possible][1])
      try:
        print("Accumulator has the value:",run(test_instruction))
      except RuntimeError:
        pass

if __name__ == '__main__':
  main()