# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

import math
from functools import reduce

def aoc(filename):
  instructions  = ""
  steps = {}
  start_nodes = set()
  end_nodes = set()
  with open(filename, "r") as f:
    for i, line in enumerate(f):
      if i == 0:
        instructions  = line.strip()
      elif i == 1:
        pass
      else:
        steps[line[0:3]] = (line[7:10], line[12:15])
        if line[2] == "A":
          start_nodes.add(line[0:3])
        if line[2] == "Z":
          end_nodes.add(line[0:3])

  initial_steps = walk(steps, instructions, start_nodes)
  end_node_steps =  walk(steps, instructions, end_nodes)
  # These were the pairs of vals and first Z they meet:
  # {'RXA': (19783, 'QCZ'), 'AAA': (18157, 'ZZZ'), 'QFA': (12737, 'PQZ'), 'JSA': (19241, 'LRZ'), 'QLA': (16531, 'VHZ'), 'RLA': (14363, 'JJZ')}
  # {'ZZZ': (18157, 'ZZZ'), 'QCZ': (19783, 'QCZ'), 'VHZ': (16531, 'VHZ'), 'PQZ': (12737, 'PQZ'), 'JJZ': (14363, 'JJZ'), 'LRZ': (19241, 'LRZ')}  

  return lcm(initial_steps.values())


# Lowest common multiplier, thank you: https://stackoverflow.com/a/70489271
def lcm(arr):
  l = reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
  return l


def walk(steps, instructions, start_nodes):
  initial_steps = {}
  for step in start_nodes:
    curr_step = step
    i = 0
    while True:
      s = instructions[i % len(instructions)]
      if s == "L":
        new_step = steps[curr_step][0]
      elif s == "R":
        new_step = steps[curr_step][1]
      i+=1
      if new_step[-1] == "Z":
        # initial_steps[step] = (i, new_step)
        initial_steps[step] = i
        break
      curr_step = new_step
  return initial_steps



testaoc1 = aoc("test3.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 6

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")

