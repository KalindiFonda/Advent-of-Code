# Beware, code written in 6am conditions full of sleepy and stressure, although, except for that rougue cards list definition, i was feeling quite good about what I was doing.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

from collections import Counter
from functools import cmp_to_key

cards = [] # I had to run test and data separately (cry)
def aoc(filename):
  total = 0
  with open(filename, "r") as f:
    for line in f:
      line = line.strip("\n").split(" ")
      cards.append((line[0], hand_poimts(line[0]), int(line[1])))

  sorted_cards = sorted(cards, key=cmp_to_key(compare))

  "(765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5)."
  l = len(cards)
  for i, c in enumerate(sorted_cards):
    total  += c[2] * (l - i)
  
  return total

def hand_poimts(hand):
  vals = Counter(hand)
  
  # deal with the joker
  j_val = 0
  if "J" in vals:
    if vals["J"] == 5:
      pass
    else:
      j_val = vals["J"]
      del vals["J"]
  max_val = max(vals, key=vals.get)[0]
  vals[max_val] = vals[max_val] + j_val
  
  # all 5 the same
  if len(vals) == 1:
    return 1
  # 4 + 1
  # 3 + 2
  if len(vals) == 2:
      if 4 in vals.values():
        return 2
      else:
        return 3
  # 3 + 1 + 1
  # 2 + 2 + 1
  if len(vals) == 3:
    if 3 in vals.values():
      return 4
    else:
      return 5
  # 2 + 1 + 1 + 1
  if len(vals) == 4:
    return 6
  # 1 + 1 + 1 + 1 + 1
  if len(vals) == 5:
    return 7
  print("shouldn't happen")
  
  
def compare(hand1, hand2):
  if hand1[1] > hand2[1]:
    return 1
  elif hand1[1] < hand2[1]:
    return -1
  """A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2."""
  d = {"A":14, "K":13, "Q":12, "T": 10, 
       "9": 9, "8":8, "7":7, "6": 6, "5": 5, 
       "4" : 4, "3":3,  "2":2, "J": 1}
  
  for i in range(5):
    h1 = int(d[hand1[0][i]])
    h2 = int(d[hand2[0][i]])
    if h1 == h2:
      pass
    elif h1 > h2:
      return -1
    elif h1 < h2: 
      return 1
  return 0
      

testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 5905

# textaoc2 = aoc("text.txt")
# print(textaoc2, "result 2 text")
