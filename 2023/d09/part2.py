# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.


def aoc(filename):
  total = 0
  nums = []
  with open(filename, "r") as f:
    for line in f:
      nums.append(list(map(int, line.strip("\n").split(" "))))

  for i, n in enumerate(nums):
    total += get_last_value(n)

  return total

def get_last_value(nums_list):
  first_vals = [nums_list[0]]

  next = True
  while next: 
    hold = []
    next = False
    for i,e in enumerate(nums_list):
      if i == len(nums_list) - 1:
        pass
      else:
        if i == 0:
          first_vals.append( nums_list[i+1] - e)
        v = nums_list[i+1] - e
        hold.append(v)
        if v != 0:
          next = True
    nums_list = hold

  curr_sum = 0
  for val in first_vals[::-1]:
    curr_sum = val - curr_sum
  return curr_sum


testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 2

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
