
https://adventofcode.com/2023/day/12

[🌟 Day 12 🌟](https://adventofcode.com/2023/day/12)


What a monster today.

But the mood and motivations were there, so I kept going at it until it gifted me those two coveted stars. Look at them:

###     🌟 🌟

how pretty.


#### Thinking process

After a bit of poking around the data, seeing if there are ways to extract large blocks, or unique opportunities, it felt like it would be too many particular cases, so I figured there must find a solution that would work for all cases.

I think I soon figued out THE solution, but it took me many many hours to optimize, polish out all the bugs, make the memoisation actually work, which actually happened through a few rewrites with the goal of simplifying the code.

Part 1:

The solution was to navigate down the springs string (ask how often I wrote string instead of springs, many, many), and for each character there were mainly 3 options (let's go recursion!): 
1. if it's a `.` go to the next character.
2. if it's a `#` go to the next character, while reducing 1 from the first element in the nums list
3. if it's a `?` branch out to two calls: the `.` case and the `#` case

I also kept checking if it was an invalid string or if it was a completed string.
This was somewhat fiddly, and probably a source of some buggitybugs (maybe)

Part 2:
2 optimisations from the above:
1. `from functools import cache` The function call parameters being a tuple of the numbers, the remaining springs string, and the valid string so far. Far from optimal in terms of counting the springs and recreating strings and etcetc, but comparatively to all the branching possibilities it was a party!
2. instead of moving by one character when hitting a possible broken spring (`#` or `?`) I checked & moved for a whole block of characters (as in whatever the distance in the first num list was).

It wasn't working, and then I kept cleaning things up, and then eventually it was working.


The final branch pruning:
- if the amount of potential damaged springs available is smaller than the sum of all the numbers in the num list
- if the length required to cover all the nus in my list is larger than the springs length
- if there are no more potential broken springs or no springs at all, but still some numbers to deal with
- if the length of the block didn't match up the number (either too short or too long)

The fruity branches:
- no more numbers in the list, and no more broken springs on the horizon

That's it.



#### Issues



#### Things I thought about afterwards:

People are talking of DP, but not sure I understood it yet.


#### Funny

Time to go to the european version of onsens, I had planned to go to the pool and sauna before, and now it feels like earned it.