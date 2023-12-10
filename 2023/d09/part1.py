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
  last_vals = [nums_list[-1]]
  
  next = True
  while next: 
    hold = []
    next = False
    for i,e in enumerate(nums_list):
      if i == len(nums_list) - 1:
        last_vals.append(e - nums_list[i-1])
      else:
        v = nums_list[i+1] - e
        hold.append(v)
        if v != 0:
          next = True
    nums_list = hold
  
  return sum(last_vals)


testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 114

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
