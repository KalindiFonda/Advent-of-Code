# This code was not written at 6am anymore, but I don't feel like the disclaimer should be any different, with the AoC days stacking up, the holiday festivities ramping up and the exhaustion and mind fog increasing it was pretty hard to focus.

# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

from collections import deque
from math import lcm

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

  step = 0
  count, counth = -1, -1
  counts = []
  to_do  = (m for m in modules["broadcaster"]["next"])
  # the hardcoded entry points
  to_do = {'lp', 'fn', 'tp', 'zz'}
  new_to_do = {'lp', 'fn', 'tp', 'zz'}

  m = ""
  while len(counts) != 4:
    # if step % 100000 == 0:
    #   print(m, step, count, counth)
    step+=1
    queue = deque()
    for m in to_do:
      queue.append((m, "l", "broadcaster"))
      count, counth = travel(queue) 
      # counth is not actually necessary, it's a leftover from the previus iteration
      if count == 1:
        counts.append((m, step))
        new_to_do.discard(m) 
    to_do = new_to_do.copy()

  return lcm(*[c[1] for c in counts])


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
  count = 0
  counth = 0
  while queue:
    curr, pulse, parent = queue.popleft()
    # hardcoded exit points:
    if curr in ["vb", "vm", "kv", "kl"]:
        if pulse  == "l":
          count +=1
        if pulse == "h":
          counth +=1
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
  return count, counth



modules = {}
textaoc2 = aoc("text.txt")
print(textaoc2, "result text")

