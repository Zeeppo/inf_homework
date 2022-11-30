from fnmatch import fnmatch

for i in range(0, 10**5):
    if fnmatch(str(i**2), "4*1?009") and i**2<=10**10:
        print(i, i**2)