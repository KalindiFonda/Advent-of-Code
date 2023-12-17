
https://adventofcode.com/2023/day/14

[🌟 Day 14 🌟](https://adventofcode.com/2023/day/14)



#### Thinking process

Part 1. 

There was no need to move any potatoes in this situation.

If there were no walls between a rock and the top, the rock was basically at i = 0 which in terms of points is len column.
And the next rock was i = 1 (points = len of the column - 1)

If we encounter a wall the next spot under it becomes the next possible top spot for a rock, so that becomes the i.


Part 2.

I created functions that rotate and drop rocks to their respective bottom spots on each rotation. I did one for each direction, and ran it a billion times. 

Well, I ran it only a couple, because the whole thing would take 400 days. Easy. 

So, I had to figure something else out. If we learned anything from a few days ago, is that there might be cycles.


I did it by creating a dictionary of all the weights I was seeing while rolling the grid. At some point the length of the dictionary wasn't increasing any more, and that was basically the number of different configurations we were seeing. 

```python
cycle_weights = {} # weight: (prev_occurance, rate (aka cycle frequency), first_seen)
```

I printed the number of weights, and realized they increase only up to 130. Same with the test case, only 7 weights, and the winning value had 6 as the start of the cycle.

Pseudocode during challenge:
```python
  # find num of cycles & start loop of cycle, 
  # then 1 bil - start cylcle if devided by cycle rate equals full num all good!
  # (n-6)/7 should be an int, 6 is start of cycle num, 7 is cycle len/rate
```

I figured I need to run the rotations more than one cycle, so I settled on 300 (a solid 2 times and a little more). I didn't need to actually check if `len(cycle weights) == prev_len_cycles`, because 300 was enough. I am still thinking what I could have done here to figure out when to stop rolling (instead of printing the number of weights while rolling for a while). Maybe something along the lines of running it double to the current max loop, with an initial dose of rolls. 🤷‍♀️

I then calculated `(1_000_000_000-first_seen_this_weight) / rate` and if it was an int, then I printed it out as it was a candidate. To be fair I was assuming I'll get one value, but both in the test and actual data, it returned 2 weights (and in both the bigger was the expected value, I suspect it had something to do with the low first sighting number of the smaller ones, and if I just calculated it with the last sighting number it would work). 

Given that it was just two values I figured I can try both of them and it'll still be faster than me figuring out what's wrong, and then the first - the bigger one - that I picked was the right one, so fine I'll take my star. I would have probably tried to understand what happens before the cycles kick in, and how to determine when to stop. But that wasn't necessary 🌟🤣


#### Issues



#### Things I thought about afterwards:


Sometimes I use paper to think it through, and often I also have little pseudocode instuctions or steps I need to do, and then I write code along it. 

I also copy chunks of challenge instructions to use as a railing for what I need to do or example data to have it handy when I am working through the code.
