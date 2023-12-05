# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

def aoc(filename):
  with open(filename, "r") as f:
    total = 0
    for line in f:
      curr_win = 0.5
      line = line[line.find(":") + 2:].strip()
      line = line.replace("  ", " ") # is this enough
      num_blocks = line.split(" | ")
      winning_numbers = set(map(int, num_blocks[0].split(" ")))
      my_numbers = set(map(int, num_blocks[1].split(" ")))
      for n in my_numbers:
        if n in winning_numbers:
          curr_win *= 2
      if curr_win != 0.5:
        total+=curr_win

  return total


testaoc1 = aoc("test.txt")
print(testaoc1, "result test")
assert testaoc1 == 13

textaoc1 = aoc("text.txt")
print(textaoc1, "result text")
