def F(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return F(n/2)-2
    elif n > 0 and n % 2 != 0:
        return 2+F(n-1)
chet = 0
for i in range (1000):
    #print(F(i))
    if F(i) == -2:
        chet += 1
print(chet,' the end')