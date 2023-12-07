# Beware, code written in 6am conditions full of sleepy and stressure, although, except for that rougue cards list definition, i was feeling quite good about what I was doing.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

from collections import Counter
from functools import cmp_to_key

cards = [] # FUCK ME
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
  """
  Five of a kind, where all five cards have the same label: AAAAA
  Four of a kind, where four cards have the same label and one card has a different label: AA8AA
  Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
  Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
  Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
  One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
  High card, where all cards' labels are distinct: 23456"""
  vals = Counter(hand)

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
  d = {"A":14, "K":13, "Q":12,  "J": 11, "T": 10, 
       "9": 9, "8":8, "7":7, "6": 6, "5": 5, 
       "4" : 4, "3":3,  "2":2}
  
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
assert testaoc1 == 6440

textaoc2 = aoc("text.txt")
print(textaoc2, "result 2 text")

