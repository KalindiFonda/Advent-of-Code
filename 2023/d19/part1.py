# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

# x: Extremely cool looking
# m: Musical (it makes a noise when you hit it)
# a: Aerodynamic
# s: Shiny

def aoc(filename):
  total = 0
  with open(filename, "r") as f:
    part1 = True
    vals = []
    steps = {}
    for line in f:
      curr_instr = []
      parent = line[:line.find("{")]

      if line == "\n":
        part1 = False
      elif part1: 
        rem_str = line[line.find("{")+1:-2]
        while rem_str:

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
            rem_str = rem_str[rem_str.find(",") + 1:]
          else: 
            second_option = rem_str[rem_str.find(",") + 1 : ]
            rem_str = ""
          curr_instr.append([curr_part, comparison, curr_num, first_option, second_option])
        steps[parent] = curr_instr
      else:
        line = line.strip("\n")[1:-1]
        val = line.split(",")
        curr_vals = {}
        for v in val:
          curr_vals[v[0]] = int(v[2:])
        vals.append(curr_vals)
        
  count = []
  for v in vals:
    count.append(travel(v, steps))
  for c in count:
    total += sum(c)

  return total

mach_parts = ["x", "m", "a", "s"]
def travel(parts, steps):
  next_step = "in"
  curr_i = 0
  while next_step != "R" and next_step != "A":
    if curr_i == 0:
      curr = steps[next_step]
    
    machine_part = curr[curr_i][0]
    comparison = curr[curr_i][1]
    num = curr[curr_i][2]
    comp_true = curr[curr_i][3]
    comp_false = curr[curr_i][4]
    if comparison == "<":
      comp = parts[machine_part] < num
    elif comparison == ">":
      comp = parts[machine_part] > num
    else:
      print("2, shouldn't happen")
    if comp: 
      next_step = comp_true
      curr_i = 0
      if next_step in mach_parts:
        print("this also shouldnt' happen")
    else: 
      if comp_false in mach_parts:
        curr_i += 1
      else:
        next_step = comp_false
        curr_i = 0
    next_step = comp_true if comp else comp_false

  if next_step == "R":
    return []
  elif next_step == "A":
    return list(parts.values())
  print("shouldn't happen")



testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 19114

textaoc2 = aoc("text.txt")
print(textaoc2, "result text")

