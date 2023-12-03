

https://adventofcode.com/2023/day/3

[🌟 Day 3 🌟](https://adventofcode.com/2023/day/3)




#### Thinking process

I printed all the characters first and put them into a set, so that I can use it for checking if it's a special char or not.

Haha, it's just a few hours later, but I had to look at my code to see how I worked through it 😅

(Part 1) So, to store the locations of the special characters I created a dictionary with keys as the y coordinate, and a list of corresponding xs in a list as the value.


Then I read through the lines again, and read out the numbers by checking the next few characters after finding one and reading them into an int.

(part 1) With the number and its start and end location I checked a box one space further out to see if there are any characters.

(part 2) 
The difference is that instead of storing all the characters I (hmmmmm) make the more convoluted version of pt1 location of special character ("*") but that does the same thing haha

And finally, a gears dictionary, where each time I find a  number with a special char, I create a dictionary entry (with the char coordinates as keys and num as value) and if we find a number with the same special char, that's out pair to multiply. 


#### Issues
pt1: some numbers were repeating twice,
pt2: I messed up with how big the box with the max_x, I think there was no need to increase it by two, because the new_x was already over the number.

And omg the internet! Had issues, and so it took me a while to get the results, run stuff, first time I was like maybe my replit life is no good.


#### Things I thought about afterwards:

It's funny to see how I went this extra route of changing my original char holding data structure to account for the new requirements, and then totally didn't need it.

