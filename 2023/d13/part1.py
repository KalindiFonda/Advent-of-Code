# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.


def aoc(filename):
  total = 0
  with open(filename, "r") as f:
    mirrors = []
    curr_mirror = []
    for line in f:
      if line == "\n":
        mirrors.append(curr_mirror)
        # An example of how I was learning about the shape of the input data. 
        # When I have a question like this I drop a print statment with my info request, and they help me decide what next. 
        # if len(curr_mirror) % 2 != 0:
        #   print("not even height")
        curr_mirror = []
      else:
        curr_mirror.append(line.strip())
      # if len(line.strip()) % 2 != 0:
      #   print("not even line")        
    mirrors.append(curr_mirror)
  for mirror in mirrors: 
    total += find_reflection(mirror)
  return total

def find_reflection(mirror):
  sides = 0
  # try vertical reflection
  for x in range(0, len(mirror[0])-1):
    x1 = x
    x2 = x+1
    next = False
    while not next: 
      for y in range(len(mirror)):
       if mirror[y][x1] != mirror[y][x2]:
        next = True
        break
      x1 -= 1
      x2 += 1
      if not next and (x1 < 0 or x2 >= len(mirror[0])):
        return x + 1

  # try horizontal reflection
  for y in range(0, len(mirror)-1):
    y1 = y
    y2 = y+1
    next = False
    while not next: 
      for x in range(len(mirror[0])):
        if mirror[y1][x] != mirror[y2][x]:
          next = True
          break
      y1 -= 1
      y2 += 1
      if not next and (y1 < 0 or y2 >= len(mirror)):
        return (y + 1) * 100
  return sides



testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 405

# textaoc2 = aoc("text.txt")
# print(textaoc2, "result text")


