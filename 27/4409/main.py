from math import gcd
with open(r"27-A.txt") as file:
  text = file.readlines()
  k = text[0]
  k = k.split(" ")[1]
  den =[]
  text.pop(0)
  text.sort()
  big = 0
  for _1 in text:
    for _2 in text:
      for _3 in text:
        if gcd(int(_1),int(_2),int(_3))>big:
          big = gcd(int(_1),int(_2),int(_3))
          print(big)