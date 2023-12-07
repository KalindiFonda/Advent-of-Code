
https://adventofcode.com/2023/day/7

[🌟 Day 7 🌟](https://adventofcode.com/2023/day/7)



#### Thinking process

Created comparison function that 
1. Parses how well they rank based on number of the same cards (hand vs hand)
2. then compare card by card.

Use my comparison function in python sort function.

```python
sorted_cards = sorted(cards, key=cmp_to_key(compare))
```

and the compare function takes two parameters to compare, and then outputs 0 if they are the same, and a negative or positive number if they are bigger or smaller (the -/+ indicates the dirction of sortage).


Oh and for part 2: 

I changed the value of J to 1 and added the count of Js to the card with the most counts in the counter dictionary.



#### Issues

RAAAAAAAAGEEEEE! 

I defined the card list outside my function, so when I ran the second call to run on the of actual data it already contained the test data. 25 minutes of comparing card pairs 🤣 


#### Things I thought about afterwards:

Commiting this one early, lets see what people say later in the day.

Suggestions: 
```python
max_val = max(vals, key=vals.get)[0]
# to
max_val = vals.most_common(1)[0] 
```

