global n
def F(n):
    if n > 15:
        return n
    else:
        return 2*F(n+1)+5*n+2
print(F(2))

            
    

    
