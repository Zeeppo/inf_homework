def F(n):
    if n < 2:
        return 1
    elif n >= 2 and n % 3 == 0:
        return F(n/3)+1
    elif n >= 2 and n % 3 != 0:
        return F(n-2)+5
k = 0
while True:
    k += 1
    if F(k) == 73:
        print(k)
        break