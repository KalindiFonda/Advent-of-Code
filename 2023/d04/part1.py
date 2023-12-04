
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
