def F(n):
    if n > 25:
        return 2*n*n*n+n
    elif n <= 25:
        return F(n+2)+2*F(n+3)
print(sum(map(int,str(F(2)))))