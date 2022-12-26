with open(r"27-B.txt") as file:
  text = file.readlines()
  minodd=111110
  mineven=11111110
  pari=0
  kodd=0
  keven=0
  text.pop(0)
  for _ in text:
    if int(_)% 2 ==0:
      if int(_)>minodd:
        pari += kodd
      mineven = min(int(_),mineven)
      keven+=1
    if int(_) % 2 != 0:
      if int(_) > mineven:
        pari += keven
      minodd = min(int(_), minodd)
      kodd += 1
  print(pari)

