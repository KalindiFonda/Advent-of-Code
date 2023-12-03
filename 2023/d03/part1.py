
chars = {'+', '*', '@', '%', '&', '$', '#', '/', '-', '='}

def aoc1(filename):
  char_map = {}
  total_sum = 0
  with open(filename, "r") as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
      for x, char in enumerate(line.strip()):
        if char in chars:
          if y in char_map:
            char_map[y].append(x)
          else:
            char_map[y] = [x]
    for y, line in enumerate(lines):
      x = 0
      while x < len(line.strip()):
        if line[x].isdigit():
          new_x, num = check_next(line, x)
          if check_if_sign(x, new_x, y, lines, char_map):
            total_sum += num
          x = new_x 
        x+=1
  return total_sum

def check_if_sign(x, new_x, y, lines, char_map):
  min_y = y-1 if y-1 >= 0 else 0
  max_y = y+2 if y+2 <= len(lines) else y+1
  for yi in range(min_y, max_y):
    if yi in char_map:
      min_x = x-1 if x-1 >= 0 else 0
      max_x = new_x+1 if new_x+1 <= len(lines[0]) else new_x
      for xi in range(min_x, max_x):
        if xi in char_map[yi]:
          return True
  return False


def check_next(line, x):
  num = 0
  while line[x].isdigit():
    num = num * 10 + int(line[x])
    x+=1
  return x, num



testaoc1 = aoc1("test.txt")
print(testaoc1, "result test")
assert testaoc1 == 4361


testaoc2 = aoc1("text.txt")
print(testaoc2, "result text")

