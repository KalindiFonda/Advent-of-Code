
https://adventofcode.com/2023/day/15

[🌟 Day 15 🌟](https://adventofcode.com/2023/day/15)


Party brain again.

My friend had his movie premiere, oh my so proud! [Kaj + Ester forever](https://www.temporama.si/portfolio-item/kaj-ester-forever/) 

![image](kaj_pa_ester.jpg)







Lots of people I know and care worked on this, so it's beautiful for it to start its I-am-a-movie-now journey, into the embraces of the audience (mostly very excited teenage girls, who were taking pictures of the lead boy anytime he was on screen alone shrieking "oh, he's so cute". I love it when the audience is alive.)!

Anyways, chatty chatty, everyone (more or less - and why do we always give ourselves such a hard time) happy, we stayed up a while, and then after what felt like 2 minutes of sleep I snuck into the corridor to do this, not to wake up the other friend I was staying with.
As I was watching the seconds tick towards 6 am I was asking the AoC gods for an easy one!



#### Thinking process

And they must have heard something, because, haha, this is like 5 lines of code 😅 

However I didn't even realize it was so short 🤣🤣 and that's because the real challenge was reading! 


Part 1:
- parse each line, and (after parsing the instructions) get value, multiply, modulo-ize and that's it : D



Part 2:

- keep my boxes in a dictionary
- used an Ordered dictionary to hold the labels and their focal length in each of the dictionary (but actually no need, a normal dict would be ok,  I just tried and it worked) 
- for each step/segment 
    - either removed the label form the appropriate box dict
    - or added the label to the boxes
- parse(the-instructions)party

And then to get the total
- calculated the focal lens power by going through the box dictionary

The reading was especially hard here! I couldn't find how to determine which box to put the labels in. I scanned the whole thing up and down a few times. 


#### Issues

#### Things I thought about afterwards: