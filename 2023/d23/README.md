
https://adventofcode.com/2023/day/23

[🌟 Day 23 🌟](https://adventofcode.com/2023/day/23)


One interesting thing, when I am cleaning code to post it (especially in these later days), and even though I delete only commented out things and print statements, it's impressive how much code I delete. All the random tries that didn't amount to anything, but also all the random variables that were meant to be something but lost their importance (and usefulness) somewhere on the way. Especially as mental clarity vanes, so does the clarity, conciseness and directedness of the code.


#### Thinking process

Ah yeah, strolls in the garden.

Part 1, bfs and putting into a queue each step along with the current count and a copy of the visited spots so far, until the end of times, while keeping track of the lenght of successful paths and then returning the longest one.


Part 2:

How long would forever take on this one? A long time. I actually did end up leaving the part1 implementation running for a few days, before I was able to sit down to tackle this problem again. (I mean I left it running until I had my star safely in hand, and only then, with a sense of cerimony CTRL+Cd the old terminal window.)


The culprit to the increase in options were the unidirectional slides that were now just a normal interesection with its many options. 
Big stretches of garden walks were actually straight, where no other options were available except for the only one that hasn't been walked yet. The intersection points however held in them the secret to the longest hike and optimisation too. 

I understood pretty "early" on that I needed to create nodes out of the intersetions with info of the steps between them and the next node. BUT for the life of me the code didn't want to bend to my will. And so I flailed around like those inflated homoids in front of car dealearships, until eventually I got the relationships (between the nodes) that I wanted. Another bfs to get the longest paths and that was it. A solid few seconds instead of eternity.





#### Issues



#### Things I thought about afterwards: