
https://adventofcode.com/2023/day/6

[🌟 Day 6 🌟](https://adventofcode.com/2023/day/6)


Today was the first day when I was properly sleepy. Between a broken glass and cloudy brain I managed to get together quite well. But when I look at my notes they are a hillarious mess (like "Loser smaller, loser winner", or a straight line with an if win in the middle), I am seriously surprised I got as far as I did  🤣


#### Thinking process

I spent a solid amount of time parsing the data, when it could have been a simple 2 line copy paste 🤣

Part 1 I did the iterative process on each potential value from 0 up to the distance (probably could have stopped a while before, hmmm I wonder if that would have helped with the brute-force approach working on pt2 as well?)
`(time[i] - speed) * speed > distance[i]`

For part2 I ran with the code from part 1, but that didn't work, so I was like must be binary search it's a lot of numbers and I need to find some number that had a simple bigger or smaller quantifier. 

I basically did one part (for the lowest winner value), and then I copy pasted it to use it for the highest winner value.

And then as I was trying to see if my binary search works, I got some values, and I manually (as in copy pasting and with a print statement) tried subtracting one from another. The first one wasn't it, but the second 60s later was correct. 


#### Issues

When halving the value space on each round I should have not had both - 1 and + 1:

```python
if (time - speed) * speed < distance:
    min = speed + 1
else: 
    max = speed - 1
```
which meant that they would never be the same (breakout condition).  So I had to give it a breaking point `(if count == 100)`.

And then I manually subtracted the various options. 
Drama! 


Also AoC panik! 



#### Things I thought about afterwards:

Some people said their check for each speed solution worked on pt2 as well, I wasn't this "lucky" haha, but then I got to implement a stressy binary search so maybe I am lucky for that.

And then there were people that solved it with a matemathical formula! O(1) baby! 

Good effort! 
