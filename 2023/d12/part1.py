# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

# Part 2 is cleaner, i was battling bugs and rewrote stuff a milion times, so I feel that one has less random extra stuff.


springs_so_far = set()
og_len_of_string = 0
def aoc(filename):
  global springs_so_far, og_len_of_string
  with open(filename, "r") as f:
    total = 0
    for line in f:
      springs_so_far = set()
      og_len_of_string = len(line)
      springs, nums = line.strip("\n").split(" ")
      nums = list(map(int,nums.split(",")))
      og_len_of_string = len(springs)
      is_num = False
      curr_val = parse(nums, springs, "", is_num)
      total += len(springs_so_far)
  return total



# cache!
def parse(nums, springs, curr_string="", is_num=False):
  global springs_so_far, og_len_of_string
  # an example of my debugging hahaha.
  # Found something suspicious in my printouts, and then caught it like this
  # if curr_string == ".###.#":
    # print("WhaaaaatWhaaaaatWhaaaaatWhaaaaatWhaaaaatWhaaaaatWhaaaaatWhaaaaatWhaaaaatWhaaaaatWhaaaaat")
  if nums == []:
    print("shouldn't happen, empty nums")
  if nums == [0]:    
    if springs.find("#") == -1:
      for i in range(len(curr_string), og_len_of_string):
        curr_string += "."
      springs_so_far.add(curr_string)
      return 1
    return 0
  if springs == "":
    return 0
  if springs.find("#") == -1 and springs.find("?") == -1:
    return 0
  if nums[0] == 0:
    if springs[0] == "#":
      return 0
    if springs[0] == "." or springs[0] == "?":
      return parse(nums[1:], springs[1:], curr_string + "." , False)
    return 10000000
  if springs[0] == "#":
    nums[0]-=1
    return parse(nums, springs[1:], curr_string + "#", True)
  if springs[0] == "?":
    if is_num:
      nums[0] -= 1 
      return parse(nums, springs[1:] , curr_string + "#" , True)
    else:
      nums2 = nums.copy()
      nums2[0]-=1 
      return parse(nums, springs[1:] , curr_string + ".", False ) + parse(nums2, springs[1:] , curr_string + "#", True )
  if springs[0] == ".":
    if is_num:
      return 0
    return parse(nums, springs[1:] , curr_string + ".", False )
  # I also create these print statements for situations that according to my understanding of the code shouldn't happen.
  print("Shouldn't happen")
  return 100000000


## Created the examples for the single lines to see how it works
# print(parse([1, 1, 3], '???.###', ""), 1)
# print(parse([1, 1, 3], '.??..??...?##.', ""),4 )
# print(parse([1, 3, 1, 6], '?#?#?#?#?#?#?#?', ""), 1)
# print(parse([4, 1, 1], '????.#...#...', ""), 1)
# print(parse([1, 6, 5], '????.######..#####.', ""), 4)
# print(parse([3, 2, 1], '?###????????', ""), 10)



testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 21

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")


# 10145 too high

#### part 1

# """
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# """

# """
# ???? 1,1 -> that should be two
# """
# springs_so_far = set()
# def aoc(filename):
#   global springs_so_far
#   with open(filename, "r") as f:
#     total = 0

#     for line in f:
#       springs_so_far = set()
#       print("\n", )
#       springs, nums = line.strip("\n").split(" ")
#       nums = list(map(int,nums.split(",")))
#       is_num = False
#       curr_val = parse(nums, springs, "", is_num)
#       # made test cases for myself      
#       # print(f"print(parse({nums}, '{springs}', ""), )")
#       # print("curr val", curr_val)
#       print(curr_val)
#       # for s in springs_so_far:
#       #   print(s)
#       #   print(len(springs_so_far))
#       total += len(springs_so_far)
#   return total



# # cache!
# def parse(nums, springs, curr_string="", is_num=False):
#   global springs_so_far
#   if curr_string == ".###.#":
#     print("WTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFFWTFFFFF")
#   # print(nums, springs)
#   if nums == []:
#     print("shouldn't happen, empty nums")
#   if nums == [0]:    
#     if springs.find("#") == -1:
#       print(nums, springs, "empty nums [0], no more #, 111111111111111")
#       springs_so_far.add(curr_string)
#       print(springs_so_far)
#       return 1
#     print(nums, springs, "empty nums [0], some #, 0")
#     return 0
#   if springs == "":
#     print(nums, springs, "more nums, empty string, 0")
#     return 0
#   if springs.find("#") == -1 and springs.find("?") == -1:
#     print(nums, springs, "more nums, no more # or ? in string, 0")
#     return 0
#   if nums[0] == 0:
#     if springs[0] == "#":
#       print(nums, springs, "next num, no break in string, 0")
#       return 0
#     if springs[0] == "." or springs[0] == "?":
#       print(nums, springs, "next num, break in string, next iteration")
#       return parse(nums[1:], springs[1:], curr_string + "." , False)
      
#     print("shouldn't happen")
#     return 10000000
#   if springs[0] == "#":
#     nums[0]-=1
#     print(nums, springs, "next step num, # string, next iteration")
#     return parse(nums, springs[1:], curr_string + "#", True)
#   if springs[0] == "?":
    
#     if is_num:
#       nums[0] -= 1
#       print(nums, springs, "next step num, # string, next iterationalso, num2", nums, "is num!")   
#       return parse(nums, springs[1:] , curr_string + "#" , True)
#     else:
#       nums2 = nums.copy()
#       nums2[0]-=1
#       print(nums, springs, "next step num, # string, next iteration also, is not num! and nums2 branching", nums2)   
#       return parse(nums, springs[1:] , curr_string + ".", False ) + parse(nums2, springs[1:] , curr_string + "#", True )
#   if springs[0] == ".":
#     print("what if number not finished????")
#     # print(nums, springs, "next step num, . string, next iteration")
#     return parse(nums, springs[1:] , curr_string + ".", False )
#     # return parse(nums, springs[1:])
#   print("Shouldn't happen")
#   return 100000000
    
  
  
    
  
  
#   # if nums[0] == 0:
#   #   if springs == "":
#   #     if len(nums) == 1:
#   #       print(nums, springs, " nums[0] == 0, no more string, nums = [0], 111111111111111")
#   #       return 1
#   #     else:
#   #       return 0


#   if springs[0] == ".":
#     return 0
#     # return parse(nums, springs[1:])
#   print("Shouldn't happen")
#   return 0
    
  

# # print(parse([1, 1, 3], '???.###', ""), 1)
# # print(parse([1, 1, 3], '.??..??...?##.', ""),4 )
# # print(parse([1, 3, 1, 6], '?#?#?#?#?#?#?#?', ""), 1)
# # print(parse([4, 1, 1], '????.#...#...', ""), 1)
# # print(parse([1, 6, 5], '????.######..#####.', ""), 4)
# # print(parse([3, 2, 1], '?###????????', ""), 10)
# # l = list(springs_so_far)
# # l = sorted(l)
# # for s in l:
# #   print(s)
# # print(len(springs_so_far))


# # print(parse([1, 1], '????', ""), 3)
# # print(parse([1, 1], '?????', ""), 3, "????")

# """
# ???.### 1,1,3 - 1 arrangement
# .??..??...?##. 1,1,3 - 4 arrangements
# ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
# ????.#...#... 4,1,1 - 1 arrangement
# ????.######..#####. 1,6,5 - 4 arrangements
# ?###???????? 3,2,1 - 10 arrangements

# """


# # testaoc1 = aoc("test3.txt")
# # print(testaoc1, "result 3 test")
# # assert testaoc1 == 1

# # testaoc1 = aoc("test2.txt")
# # print(testaoc1, "result 2 test")
# # assert testaoc1 == 23

# testaoc1 = aoc("test.txt")
# print(testaoc1, "result 1 test")
# assert testaoc1 == 21

# textaoc2 = aoc("text.txt")
# print(textaoc2, "result text")


