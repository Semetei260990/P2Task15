my_age = int(input("Сколько вам лет?: "))
n = 0
m = 1
if my_age % 2 == 0:
    while n < my_age:
        n += 2
        print(n)
else:
    while m < my_age:
        m += 2
        print(m)