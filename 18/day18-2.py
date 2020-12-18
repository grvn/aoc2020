#!/usr/bin/env python3
from sys import argv

def calculate(input):
  if input.find('(') == -1:
      input = [int(x) if x.isdigit() else x for x in input.split()]
      i = 0
      while i < len(input):
        if input[i] == '+':
          sum = input[i-1] + input[i+1]
          input[i-1] = sum
          del input[i:i+2]
        else:
          i += 1
      sum = input[0]
      for i in range(1,len(input),2):
        if input[i] == '*':
          sum *= input[i+1]
      return sum
  else:
    extra = 0
    first = input.index('(')
    for i,char in enumerate(input[first+1:],first):
      if char == '(': # nested
        extra += 1
      elif char == ')':
        if extra == 0:
          break
        else:
          extra -= 1
    return calculate(input[:first] + str(calculate(input[first+1:i+1])) + input[i+2:])

def main():
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  print(sum(calculate(line) for line in input))

if __name__ == '__main__':
  main()