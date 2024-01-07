
https://adventofcode.com/2023/day/18

[🌟 Day 18 🌟](https://adventofcode.com/2023/day/18)



Ok I think this is where I started to lose the plot. I was still holding on, but barely. 
So buckle in for the implementation of part one. 

----

These write ups (starting today) are done with a few weeks delay, so my first reaction seeing the code was: "I have no idea what's going on." and it definitely didn't look very comforting when I saw print messages such as: "emergency", "second_emergency", "strange", "strange pipe behaviour". As memory started fading out of the fog, I actually think these were just hand rails making sure my assumptions about the data were correct, basically if everything is as I expect it to be, these print statements shouldn't pop up.


#### Thinking process

Travelling through the grid to create the outline was fairly straightforward, I created a grid a bit bigger than what the max and min values in each direction where (I printed those out and used the values).

Then I thought I could do a check down right or up left and mark as fillled the ones that fit the requirements. 

But I just couldn't make it work, not sure why. Anyways I was desperate, so I went to day 10 and copy pasted the pipe function! To make that work, I transformed my edges into the pipe values, |, -, F, J, L, 7. It was really not very handy but it worked and a star is a star.

For part 2: 

One thing I remember learning about during day 10 was that people used the poligon area to solve their task. And if I remember correctly the long lines made it impossible to actually draw the grid, so poligon to the rescue. I found a few different implementation of the poligon area on stack overflow, and even though the writers were promising differences between them they all resulted in the same (but incorrect) value for me (maybe the data had no negative values, or no crossing or other things that would complicate the thing). 

I figured there was probably something that wasn't taken into consideration in this number. Usually poligon perimeters are a thin line that has no area of it's own, but in this case our poligon was also squares. With some trial and error with the example case, I figured that the formula that accounts for that is: 

```python
lines/2 + len(y) / 2 + 1
```

🤔🤨🧐
lines being what?
y being the number of coordinates?


which basically comes out to be

```python
perimeter / 2 + 1
```

but through some creative stuff in the code before, lines + len(coordinates) is basically the perimeter, maybe.


Long live the AoC stars.





#### Issues



#### Things I thought about afterwards:

This was a pretty nice do-it-by-hand description, that if nothing else was a nice way to scribble things on paper to create some kind of ✨intuition✨ https://www.wikihow.com/Calculate-the-Area-of-a-Polygon#Finding-the-Area-of-Irregular-Polygons
