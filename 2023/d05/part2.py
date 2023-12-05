# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.


# Pseudocode
# check paths from lowest location, backwards
# check if number exists in the ranges of seeds


steps = []
seeds = []
def aoc(filename):
  global seeds
  with open(filename, "r") as f:
    new_mapping = {}
    for i, line in enumerate(f):
      if i == 0:
        seeds = list(map(int, line[7:].strip("\n").split(" ")))
      if line == "\n":
        if new_mapping:
          steps.append(new_mapping)
        new_mapping = {}
      if line[0].isdigit():
        vals = list(map(int, line.strip("\n").split(" ")))
        new_mapping[vals[0]] = [vals[0]+vals[2], vals[1]-vals[0]]
    steps.append(new_mapping)
  return try_this()


def check_in_range(num):    
  for i in range(0, len(seeds), 2):
    if num >= seeds[i] and num <= seeds[i]+seeds[i+1]:
      return True
  return False

def try_this():
  for i in range(510_109_797): # this was my previous lowest location
    seed = i
    for step in steps[::-1]:
      for start, extra in step.items():
        stop, diff = extra
        if seed >= start and seed < stop:
          seed += diff
          break
    if check_in_range(seed):
      return i
    

testaoc1 = aoc("test.txt")
print(testaoc1, "result test 1")
assert testaoc1 == 46

textaoc2 = aoc("text.txt")
print(textaoc2, "result text 2")
