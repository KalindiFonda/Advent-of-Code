
https://adventofcode.com/2023/day/1

[🌟 Day 1 🌟](https://adventofcode.com/2023/day/1)


I was actually worldwide 800something, which is the best ever.

I mean I guess I still read some of the story, and I haven't really polished my data getting and all that, and I always found it to be part of my aoc ritual.

#### Thinking process

Look until you find the first digit, and then look from the back until first digit, then next.

For part 2 on top of the above check from current char, look forward or backward x characters to see if it's a string mapping to a digit.


#### Things I thought about afterwards:
I keep forgetting about this guy: 
`line[::-1]`

Instead of writing this 3 times, loop through 3-5, and see if that is in digits.
```
if line[i:i+3] in  digits_3:
    n = int(digits_3[line[i:i+3]])* 10
    break
```


