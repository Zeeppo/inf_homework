from time import perf_counter
from random import randint
def F(n):
    global k
    print('*', end='')
    k += 1
    if n >= 1:
        print('*', end='')
        F(n-1)
        F(n-3)
        print('*',randint(1,1),end='') #я не знаю почему, но добавление randint ускорило выполнение примерно в 4.3 раза
        k += 2
time1 = perf_counter()
k = 0
F(40)
print('\n',k)
print('Время выполнение программы = ', perf_counter()-time1,' сек')



