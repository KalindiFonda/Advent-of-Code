
https://adventofcode.com/2023/day/8

[🌟 Day 8 🌟](https://adventofcode.com/2023/day/8)


#### Thinking process

Fun one again! 
Part 1 was swift, part 2 took a solid fiddle to figure out to do. 

Part 1, I created a dictionary with the left/right nodes, and then travelled down the dictionary, until I found the node I wanted.

Part 2 was a journey. Of course I tried the above, but one window was running that while I was trying to figure out alternative solutions, and there was no sign of result. 
Then I figured I could maybe find the points when the various start points get to a Z value, and then find matching values [lots of fiddling here]. But at some point when I printed them out, I was like hmmmm, they 1. seem related to the result, 2. end and start arrival "stations" were also related, which is still a bit confusing, but I think it goes like this:

The As stations needed to take X steps to get to the first Z station, and than that same Z station needed exactly X steps to get to the next Z station which was itself
```python
These were the pairs of vals and first Z they meet:
{'RXA': (19783, 'QCZ'), 'AAA': (18157, 'ZZZ'), 'QFA': (12737, 'PQZ'), 'JSA': (19241, 'LRZ'), 'QLA': (16531, 'VHZ'), 'RLA': (14363, 'JJZ')}
{'ZZZ': (18157, 'ZZZ'), 'QCZ': (19783, 'QCZ'), 'VHZ': (16531, 'VHZ'), 'PQZ': (12737, 'PQZ'), 'JJZ': (14363, 'JJZ'), 'LRZ': (19241, 'LRZ')}
```  


And then when I got the lowest common multiplier and that was that.


#### Issues

I think I am in a "sweet" spot where I know there are some algo and datastructure solutions, so I go all in in trying to remember, figure out and then implement something. 

When in fact there might be a simpler/logical/how-would-a-human do it solution sometimes, which I miss because I go all into the "what was that thing already". 😂

It's that equivalent to the learning how to dance story. Like first you dance without thinking and knowing anything so you do whatever, flail your arms, to the rythm or not, yea! Then you learn some moves, and because you focus on the steps and think of the coregraphy and whatever it's more likely one trips up on ones own legs. But then (supposedly) mastery (of the new level) comes and the let go / play / ease / natural-ness comes again.

It's nice to see, though, how maybe something where I stumbled or had to figure out years ago, is now part of my dance routine.

You know:
> What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

#### Things I thought about afterwards:

Ahhhh haha I tried this: 

```python
math.lcm([1,2,3]) 
```
And got scared by the error: 
`TypeError: 'list' object cannot be interpreted as an integer`. I could have just unpacked the list 🤦‍♀️ instead I got some lcm equivalent of off stack overflow.

```python
math.lcm(*[1,2,3]) 
```