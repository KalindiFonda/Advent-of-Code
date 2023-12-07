
https://adventofcode.com/2023/day/4

[🌟 Day 4 🌟](https://adventofcode.com/2023/day/4)



#### Thinking process

Get sets out the numbers.

And then for each number check if it's in the other set. If differences in len were big, or if there were repeating nums the order might matter, but I don't think so now. Checkin if a num is in a set is O(1).

(Part1) simple count.

(Part2)
Made two lists, one with wins per card, and one with n of scratchcards for each scratchcard.

As I went through the winnings, I added the number of scrachcards won to the list of scratchcards.

(while keeping the ott num of scratchcards, which was the answer).

I think I got the for loop party right on the first go, so that's good : D





#### Issues-ish

I was fiddling with the parsing with double spaces or spaces before/after split. So had to the run>fix>run>fix dance.

Everytime there is a task that seem like it's pretty straightforward, I run along wondering if I'll trip somewhere.
And all the many for loops I had, I was just waiting 😅

The second part took a good few seconds, and it had me worried if it's time to optimize : )

#### Things I thought about (afterwards):

It's interesting, that I sometimes leave myself comments about places in the code that is suspicious and to keep it in mind if struggling.
