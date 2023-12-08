# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

def aoc(filename):
  total = 0
  instructions  = ""
  steps = {}
  with open(filename, "r") as f:
    for i, line in enumerate(f):
      if i == 0:
        instructions  = line.strip()
      elif i == 1:
        pass
      else:
        steps[line[0:3]] = (line[7:10], line[12:15])
  
  total = walk(steps, instructions)

  return total

def walk(steps, instructions):
  curr_step = "AAA"
  i = 0
  while curr_step != "ZZZ":
    s = instructions[i % len(instructions)]
    if s == "L":
      new_step = steps[curr_step][0]
    elif s == "R":
      new_step = steps[curr_step][1]
    i+=1
    if new_step == "ZZZ":
      return i
    curr_step = new_step
    
testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 2


testaoc1 = aoc("test2.txt")
print(testaoc1, "result 2 test")
assert testaoc1 == 6

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")


