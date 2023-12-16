# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

from collections import OrderedDict

def aoc(filename):
  with open(filename, "r") as f:
    for line in f:
      vals = line.strip("\n").split(",")
    boxes = {}
    for val in vals:
      deal_with(val, boxes)
  return calculate(boxes)

def calculate(boxes):
  total = 0
  for box, lenses in boxes.items():
    for i,lens in enumerate(lenses):  
      curr = box+1 
      curr *= (i+1)
      curr *= int(lenses[lens])
      total+=curr
  return total
    
def get_hash(label):
  num = 0
  for c in label: 
    num += ord(c)
    num *= 17
    num %= 256
  return num

def deal_with(vals, boxes):  
  if vals[-1] == "-":
    label = vals[:-1]
    box = get_hash(label)
    if box in boxes:
      if label in boxes[box]:
          del boxes[box][label]
  else:
    label, foc_len = vals.split("=")
    box = get_hash(label)
    if box not in boxes:
      boxes[box] = OrderedDict()
    boxes[box][label] = foc_len


testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 145

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")


