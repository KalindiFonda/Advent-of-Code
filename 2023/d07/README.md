
https://adventofcode.com/2023/day/7

[🌟 Day 7 🌟](https://adventofcode.com/2023/day/7)



#### Thinking process

Created comparison function that 
1. Parses how well they rank based on number of the same cards
2. Parse step by step, card by card.

Use my comparison function in python sort function.

```python
sorted_cards = sorted(cards, key=cmp_to_key(compare))
```

and the compare funtion takes two parameters to compare, and then outputs 0 if they are the same, and a negative or positive number if they are bigger or smaller (the -/+ indicates the dirction of sortage).


#### Issues

RAAAAAAAAGEEEEE! 

I defined a list outside my function, so when I ran the second call to aoc to run on the of data it contained the other data. 25 minutes of comparing card pairs laugh 🤣 


#### Things I thought about afterwards:

Commiting this one early, lets see what people say later in the day.
