
digits = {"one": 1, "two": 2, "six": 6, "four": 4, "five":5,   "nine": 9, "zero":0, "three":3, "seven":7, "eight": 8}


with open("text.txt", "r") as f:
  count = 0
  for line in f:
    n = 0
    for i in range(len(line)):
      if line[i].isnumeric():
        n = int(line[i])* 10
        break
      for len_d in range(3, 6):
        if line[i:i+len_d] in  digits:
          n = int(digits[line[i:i+len_d]])* 10
          break
    for i in range(len(line)-1, -1, -1): 
      if line[i].isnumeric():
        n+= int(line[i])
        break
      for len_d in range(3, 6):
        if line[i-len_d:i] in  digits:
          n += int(digits[line[i-len_d:i]])
          break
    count+=n


  print(count)
