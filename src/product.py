# l = [1.3, 2, 4.6, 6.1, -7, 10, 5.6, 19, -1.1, 0]
# for i in l:
#     print("{}".format(i))
#
#
# n = 0
# while n != len(l):
#     print(n)
#     print(l[n])
#     n = n + 1

import random

def random_generation():
    chislo = 0
    while chislo != 10:
        chislo = random.randint(0, 11)
        print("Число равно {}".format(chislo))
    print("Закочили")

random_generation()

