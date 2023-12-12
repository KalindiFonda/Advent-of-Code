# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

from functools import cache

def aoc(filename):
  with open(filename, "r") as f:
    total = 0
    for i, line in enumerate(f):
      springs, nums = line.strip("\n").split(" ")
      nums = tuple(map(int,nums.split(",")))
      vals = unfold(nums, springs)
      total += vals
  print("totoal", total)
  return total

def unfold(nums, springs):
  nums = nums * 5
  springs = springs + "?"
  springs = (springs * 5)[:-1]
  while springs.find("..") != -1:
    springs = springs.replace("..", ".")
  return parse(tuple(nums), springs)

@cache
def parse(nums, springs, curr_str = ""):

  nums_sum = sum(nums)
  min_str_len = nums_sum + len(nums) - 1
  num_hashes = springs.count("#")
  potential_num_hashes = num_hashes + springs.count("?")
  
  # end cases
  if potential_num_hashes < nums_sum:
    return 0
  if min_str_len > len(springs):
    return 0
  if not nums:
    if num_hashes == 0:
      return 1
    return 0
  if springs == "" or potential_num_hashes == 0:
    return 0

  # ? and # case, (it was fiddly to have repetition here):
  if springs[0] == "#":
    if springs[:nums[0]].find(".") == -1:
      if len(springs) > nums[0] and springs[nums[0]] == "#": # not a dot
        return 0
      curr_str = curr_str + nums[0] * "#" + "."
      return parse(nums[1:], springs[nums[0] + 1:], curr_str)
    else:
      return 0
  if springs[0] == "?":
    if springs[:nums[0]].find(".") == -1:
      new_curr_str = curr_str + nums[0] * "#" + "."
      if len(springs) > nums[0] and springs[nums[0]] == "#": # not a dot
        return parse(nums, springs[1:], curr_str)
      # branching option, one if it's a valid segment, or just next char:
      return parse(nums[1:], springs[nums[0] + 1:], new_curr_str) + parse(nums, springs[1:], curr_str)
    return parse(nums, springs[1:])

  if springs[0] == ".":
    return parse(nums, springs[1:], curr_str)
  
  print("Shouldn't happen, end")
  return 100000000


# line examples
# print(unfold([2,2,1,1,2,1], '??.???.?.?.??.???.'), 1)
# print(unfold([1, 1, 3], '???.###'), 1)
# print(unfold([1, 1, 3], '.??..??...?##.'), 16384 )
# print(unfold([1, 3, 1, 6], '?#?#?#?#?#?#?#?'), 1)
# print(unfold([4, 1, 1], '????.#...#...'), 16)
# print(unfold([1, 6, 5], '????.######..#####.'), 2500)
# print(unfold([3, 2, 1], '?###????????'), 506250)


testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 525152

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
