for i in range(10,1000000):
  a = bin(i-bin(i)[2:].count("0"))[2:]
  a = a[-3] + a[-2]+a[-1]+a
  if int(a, base = 2) > 224:
    print(int(a,base = 2))
    exit(0)