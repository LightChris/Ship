import random

lst = []
low, mx = -20, 20
a = 0
while len(lst) < 20:
    x = random.randint(-20, 20)
    if len(lst) == 0:
        lst.append(x)
    else:
        for el in lst:
            if el != x:
                a = a + 1
            if a == len(lst):
                lst.append(x)
                a = 0
                break

print(lst)
