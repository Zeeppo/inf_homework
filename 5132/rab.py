from math import gcd

for A in range(1,100):
    k=0
    for x in range(1,31):
        if not(gcd(x, 42)!=1) or not(gcd(x, 7)!=1) or x+A>=25:
            k +=1
    if k == 30:
        print(A)
        break
