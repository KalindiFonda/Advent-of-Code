
https://adventofcode.com/2023/day/13

[🌟 Day 13 🌟](https://adventofcode.com/2023/day/13)




#### Thinking process

Things were relatively straightforward and I didn't spend much time on wrong paths.

Part 1

- make the grid from each mirror, party!! grid!!!! (i opted for a list of strings - each line a string)
- for each mirror, I checked the characters pair along each pair of adjecent columns (or row but i'll explain what I did with the colums) and if they were not the same I moved onto the next pair
- If I came to the bottom of the column, and all the characte pairs were the same I moved out one line (one left for the left side, and one right for the right side) and checked the column pairs again.
- if I was about to fall off the edge of the grid it meant success so I returned that! 

Part 2

I think that's basically it: 
- Very similar process as above, but I gave it a "one strike" allowance, so it only kicked out of the check if two characters were different. 

- (useless bug inducing effort, I now know) I was changing the smudge to the opposite character, so I had to change the grid format from a list of strings to a list of lists.



#### Issues


Oh no! 

```python
mirror[y_hold][x_hold] = "." if mirror[y_hold][x_hold] == "#" else "."
```

I wrote this out and was like YOU ARE NOT GOING TO TRICK ME. I wrote the `#` so now it's the turn of the dot! 

well it tricked me 🤣

```python
mirror[y_hold][x_hold] = "." if mirror[y_hold][x_hold] == "#" else "#"
```

it's the dot in front that is assigned when the comparison is True. Anyways great way to spend some 30 mins trying to figure out why your code works on the test and not on the input (somehow for the examples given, the grid didn't need to return to the origi state - maybe that the first irregularity encountered was actually a smudge, I don't remember anymore)


So because I didn't remember anymore I went to check what this was actually doing. And let me tell you it's not doing anything 😂😭🥲🤣

I was nurturing a bug for no apparent reason. (Probably fixed something at the same time as introducing the changing line, so I thought the fix came from smudge change.)


---

The repetition was strong between the horizontal and vertical checks, but whatever function I'd get our of it was not straightforward with the x & y inverted, and that was a bit too much to try to fix it in the rush so I had to do everything twice 🤣, write bugs twice, write fixes twice...

#### Things I thought about afterwards:

