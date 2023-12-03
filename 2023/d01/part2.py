
digits_3 = {"one": 1, "two": 2, "six": 6}
digits_4 = {"four": 4, "five":5,   "nine": 9, "zero":0}
digits_5 =  {"three":3, "seven":7, "eight": 8}


with open("text.txt", "r") as f:
  count = 0
  for line in f:
    n = 0
    for i in range(len(line)):
      if line[i].isnumeric():
        n = int(line[i])* 10
        break
      if line[i:i+3] in  digits_3:
        n = int(digits_3[line[i:i+3]])* 10
        break
      if line[i:i+4] in  digits_4:
        n = int(digits_4[line[i:i+4]])* 10
        break
      if line[i:i+5] in  digits_5:
        n = int(digits_5[line[i:i+5]])* 10
        break
      
    for i in range(len(line)-1, -1, -1):
      if line[i].isnumeric():
        n+= int(line[i])
        break
      if line[i-3:i] in  digits_3:
        n += int(digits_3[line[i-3:i]])
        break
      if line[i-4:i] in  digits_4:
        n += int(digits_4[line[i-4:i]])
        break
      if line[i-5:i] in  digits_5:
        n += int(digits_5[line[i-5:i]])
        break
    count+=n
        
          
  print(count)
