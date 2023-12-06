# Beware, code written in 6am conditions full of sleepy and stressure.
# Before posting I remove print statements, unused variables, and dead-end functions and tries, otherwise I leave the code as is, because I think it's fun to see what happens under those conditions.
# For more info read the READMEs.

# test data
"""
Time:      7  15   30
Distance:  9  40  200
"""
time = 71530
distance = 940200

# data
"""
Time:        48     93     85     95
Distance:   296   1928   1236   1391
"""
time =  48938595
distance = 296192812361391


# find lowest number 
min = 0
max = time
speed = (max - min) // 2
count = 0
while True: 
  count+=1
  if max == min:
    break
  if count == 100:
    break
  speed = (max + min) // 2
  if (time - speed) * speed < distance:
    min = speed + 1
  else: 
    max = speed - 1 # should have not had both - 1 and + 1
print(min, max)


# find highest number 
min = 0
max = distance
speed = (max - min) // 2
count = 0
while True: 
  count+=1
  if max == min:
    break
  if count == 100:
    break
  speed = (max + min) // 2
  if (time - speed) * speed > distance: # the direction of this comparison is the only difference to the above block
    min = speed + 1
  else: 
    max = speed - 1  # should have not had both - 1 and + 1 (as that created two values, that I then manually subtracted) 
print(min, max)

# next step, I copy pasted the values that came out from the above mins and maxes)
# subtract the result from the highest num to the lowest num
print(41863369 - 7075226)
print(41863369 - 7075227)
