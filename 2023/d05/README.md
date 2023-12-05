
https://adventofcode.com/2023/day/5

[🌟 Day 5 🌟](https://adventofcode.com/2023/day/5)

#### Thinking process

# 😱😭

Ahhhh, it took me a solid while to even understand the data, what's happening and what we need to produce
At some point I had to climb out of bed and get some paper too, because this was not cosy blanket AoC no more.

Part 2 hit with the bilion numbers : D

It was the first day with AoC panik and cloudy brain. Nice. 

----

Basically for part 1 I took each seed and walked all the paths holding onto the lowest location value so far.

For part 2 I did the journey the other way, and started with location 0 and went back through the transformations, and once I got a seed value I checked if it existed among the ranges of seeds.


```for i in range(510_109_797):```
this was my previous lowest location, my current seed could have been bigger, but I was relatively lucky that my actual lowest location was quite low. 

So despite not coming up with some nicely optimized algo, I manage to sneak away with my two stars today 🌟🌟

#### Issues
Halfway I forgot how I was holding my data:
```{starting_number: [end_number, operation_after_fertilisation]}```
So I had to rethink throug it for part two.

And for part two, I kept the order, where destination was the key.


#### Things I thought about afterwards:

The computer gave me this suggestion: 
```python
  for i in range(0, len(seeds), 2):
    if num >= seeds[i] and num <= seeds[i]+seeds[i+1]:
      return True
  return False
```
vs

```python
  return any(num >= seeds[i] and num <= seeds[i + 1] for i in range(0, len(seeds), 2))
```
Will take a moment to see how other people did today, and see if any of the optimized paths make sense.