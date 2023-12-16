# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

def aoc(filename):
  total = 0
  with open(filename, "r") as f:
    for line in f:
      vals = line.strip("\n").split(",")
    for val in vals:
      total += deal_with(val)
  return total


def deal_with(vals):
  num = 0
  for c in vals: 
    num += ord(c)
    num *= 17
    num %= 256
  return num


testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 1320

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
