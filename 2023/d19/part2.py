# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.



# x: Extremely cool looking
# m: Musical (it makes a noise when you hit it)
# a: Aerodynamic
# s: Shiny



import string
import random




def aoc(filename):
  global steps
  with open(filename, "r") as f:
    part1 = True
    steps = {}
    for line in f:
      parent = line[:line.find("{")]
      hold_parent = parent
      if line == "\n":
        part1 = False
      elif part1: 
        rem_str = line[line.find("{")+1:-2]
        while rem_str:
          if hold_parent != parent:
            hold_parent = parent

          curr_part = rem_str[0]
          comparison = rem_str[1]

          curr_num = int(rem_str[2:rem_str.find(":")])
          rem_str = rem_str[2:]
          first_option = rem_str[rem_str.find(":") + 1 : rem_str.find(",")]
          i_bigger = rem_str.find(">")
          i_smaller = rem_str.find("<")
          if i_bigger == -1 or i_smaller == -1:
            comp_i = max(i_bigger, i_smaller)
          else:
            comp_i = min(i_bigger, i_smaller)
          if comp_i != -1:
            second_option = rem_str[rem_str.find(",") + 1 : comp_i]
            if second_option in mach_parts:
              parent = ''.join(random.choices(string.ascii_uppercase +
                 string.digits, k=5))
              second_option = parent
            rem_str = rem_str[rem_str.find(",") + 1:]
          else: 
            second_option = rem_str[rem_str.find(",") + 1 : ]
            rem_str = ""
          steps[hold_parent] = [curr_part, comparison, curr_num, 
                           first_option, second_option]
          
  match_count_start = {"x_min": 1, "x_max": 4000, 
                 "m_min": 1, "m_max": 4000, 
                 "a_min": 1, "a_max": 4000, 
                 "s_min": 1, "s_max": 4000}

  return travel( "in", match_count_start, 1)


mach_parts = ["x", "m", "a", "s"]
mach_pairs = {
  "x": ["x_min", "x_max"],
  "m": ["m_min", "m_max"],
  "a": ["a_min", "a_max"],
  "s": ["s_min", "s_max"]}


def travel(next_step, match_count, curr_count=1):
  if next_step == "R":
     return 0
  elif next_step == "A":
    return count_paths(match_count)

  # get the vals from each instruction    
  curr = steps[next_step]
  machine_part = curr[0]
  comparison = curr[1]
  num = curr[2]
  comp_true = curr[3]
  comp_false = curr[4]
  # get the name of the pair to change
  curr_mach_pair = mach_pairs[machine_part]
  if comparison == "<":
    mc_true =  match_count.copy()
    mc_false =  match_count.copy()
    mc_true[curr_mach_pair[1]] = num - 1
    mc_false[curr_mach_pair[0]] = num
    return  travel( comp_true, mc_true) +  travel(comp_false, mc_false)
  if comparison == ">":
    mc_true =  match_count.copy()
    mc_false =  match_count.copy()
    mc_true[curr_mach_pair[0]] = num + 1
    mc_false[curr_mach_pair[1]] = num
    return  travel( comp_true, mc_true) +  travel(comp_false, mc_false)

def count_paths(match_count):
  x_range = match_count["x_max"] - match_count["x_min"] + 1
  m_range = match_count["m_max"] - match_count["m_min"] + 1
  a_range = match_count["a_max"] - match_count["a_min"] + 1
  s_range = match_count["s_max"] - match_count["s_min"] + 1
  curr_count =  x_range * m_range * a_range * s_range 
  return curr_count


steps = {}
testaoc1 = aoc("test.txt")
print(testaoc1, "result  test")
assert testaoc1 == 167409079868000


textaoc2 = aoc("text.txt")
print(textaoc2, "result text")
