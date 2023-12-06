# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.



def aoc(filename):
  total = 1
  with open(filename, "r") as f:
    x = f.readline()
    y = f.readline()

    x = x[x.find(":")+ 2:].strip("\n").replace("  ", " ").split(" ")
    y = y[y.find(":")+ 2:].strip("\n").replace("  ", " ").split(" ")
    time = [int(t) for t in x if t != ""]
    distance = [int(d) for d in y if d != ""]

  for i in range(len(time)):
    curr_total = 0
    for speed in range(distance[i]):
      if (time[i] - speed) * speed > distance[i]:
        curr_total += 1
    total *=curr_total

  return total



testaoc1 = aoc("test.txt")
print(testaoc1, "result 1 test")
assert testaoc1 == 288

textaoc2 = aoc("text.txt")
print(textaoc2, "result 2 text")