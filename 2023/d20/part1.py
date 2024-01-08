# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.



from collections import deque

modules = {}
def aoc(filename):

  with open(filename, "r") as f:
    for line in f:
      mod_type = line[0]
      elements = line.strip("\n").replace(",", "").split(" ")
      if elements[0] == "broadcaster":
        curr = "broadcaster"
        mod_stren = "l"
      else:
        if elements[0][0] == "&":
          mod_stren = "l"
        else:
          mod_stren = "off"
        curr = elements[0][1:]
      next = elements[2:]
      modules[curr] = {
        "mod_type": mod_type, 
        "mod_stren": mod_stren, 
        "next": next, 
        "curr_state": {}}
  get_all_cons("broadcaster")

  n = 1000
  # n = 4

  for _ in range(n):
    queue = deque()
    count_lh["l"] += 1
    for m in modules["broadcaster"]["next"]:
      queue.append((m, "l", "broadcaster"))
    travel(queue)
  return count_lh["l"] * count_lh["h"]




"""



broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a

broadcaster
{'mod_type': 'b', 'mod_stren': 'l', 'next': ['a', 'b', 'c'], 'curr_state': []}
a
{'mod_type': '%', 'mod_stren': 'off', 'next': ['b'], 'curr_state': []}
b
{'mod_type': '%', 'mod_stren': 'off', 'next': ['c'], 'curr_state': []}
c
{'mod_type': '%', 'mod_stren': 'off', 'next': ['inv'], 'curr_state': []}
inv
{'mod_type': '&', 'mod_stren': 'l', 'next': ['a'], 'curr_state': []}
"""

def get_all_cons(module):
  seen = set()
  queue = deque()
  queue.append(module)
  while queue:
    curr = queue.popleft()
    for m in modules[curr]["next"]:
      if m not in seen: 
        queue.append(m)
        seen.add(m)
      if m not in modules:
        modules[m] = {'mod_type': '?', 'mod_stren': '', 'next': [], 'curr_state': {}}
      if modules[m]["mod_type"] == "&":
        modules[m]["curr_state"][curr] = 0
  return 0

def travel(queue):
  while queue:
    curr, pulse, parent = queue.popleft()
    count_lh[pulse] += 1
    if curr not in modules:
      print(curr, " not in modules")
    elif modules[curr]["mod_type"] == "%":
      status =  modules[curr]["mod_stren"]
      if pulse == "h":
        pass
      elif pulse == "l":
        if status == "off":
          modules[curr]["mod_stren"] = "on"
          next_stren = "h"
        else: 
          modules[curr]["mod_stren"] = "off"
          next_stren = "l"
        for m in modules[curr]["next"]:
          queue.append((m, next_stren, curr))
    elif modules[curr]["mod_type"] == "&":
      p_int = 0 if pulse == "l" else 1
      modules[curr]["curr_state"][parent] = p_int
      sum_state = sum(modules[curr]["curr_state"].values())
      next_stren = "h"
      if sum_state == len(modules[curr]["curr_state"]):
        next_stren = "l"
        
      for m in modules[curr]["next"]:
        queue.append((m, next_stren, curr))



modules = {}
count_lh = {"l": 0, "h":0}
testaoc1 = aoc("test.txt")
print(count_lh)
print(testaoc1, "result 1 test")

assert testaoc1 == 32000000

modules = {}
count_lh = {"l": 0, "h":0}
testaoc1 = aoc("test1.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 11687500


modules = {}
count_lh = {"l": 0, "h":0}
textaoc2 = aoc("text.txt")
print(textaoc2, "result text")

