def aoc(filename):
  with open(filename, "r") as f:
    wins = []
    sc = []
    for line in f:
      sc.append(1)
      line = line[line.find(":") + 2:].strip()
      line = line.replace("  ", " ")
      num_blocks = line.split(" | ")
      winning_numbers = set(map(int, num_blocks[0].split(" ")))
      my_numbers = set(map(int, num_blocks[1].split(" ")))
      count_wins = 0
      for n in my_numbers:
        if n in winning_numbers:
          count_wins+=1
      wins.append(count_wins)
    total = 0
    for i, w in enumerate(wins):
      total += sc[i]
      for s in range(sc[i]):
        for extra_sc in range(w):
          if i + extra_sc + 1 < len(wins):
            sc[i+extra_sc+1]+=1
  return total

testaoc1 = aoc("test.txt")

print(testaoc1, "result test")
assert testaoc1 == 30

textaoc1 = aoc("text.txt")
print(textaoc1, "result text")
