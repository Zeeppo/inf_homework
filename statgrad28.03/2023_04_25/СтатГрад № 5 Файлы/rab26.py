file = open(r"26.txt").readlines()[1:]
a = 80
b = 20

l = [[x for x in i.split()] for i in file]
for el1 in range(len(l)):
    l[el1] = [int(l[el1][0]), int(l[el1][1]), l[el1][2]]
l.sort()
lpr = [[el1[0], el1[2]] for el1 in l]
lot = [[el1[1] + el1[0], el1[2]] for el1 in l]
ueh = 0
pripark = 0
vr = 0
print(lpr)
ld = []
print(lot)
for i in range(10000):
    for el5 in range(len(lot)):
        if lot[el5][0] == vr:
            if lot[el5][1] == "A":
                if lot[el5][0] in ld:
                    b += 1
                else:
                    a += 1
            elif lot[el5][1] == "B":
                b += 1
        # print(lot[el5])
    for el6 in range(len(lpr)):
        if lpr[el6][0] == vr:
            if lpr[el6][1] == "A":
                if a > 0:
                    a -= 1
                    pripark += 1
                elif b > 0:
                    b -= 1
                    ld.append(lot[el6][0])
                    pripark += 1
                else:
                    ueh += 1
            elif lpr[el6][1] == "B":
                if b > 0:
                    b -= 1
                else:
                    ueh += 1
        # print(lot[el6])
    print(ld)
    vr += 1
print(pripark, ueh)
