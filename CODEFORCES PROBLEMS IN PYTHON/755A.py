# 755A
from math import *


def sieve_original(n):
    l = []
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if sieve[i] == True:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    for p in range(2, len(sieve)):
        if sieve[p] == True:
            l.append(p)
    return l


# a=10
a = 100000
z = sieve_original(a)

m = 10000
n = int(input())
"""
if n in z:
    p=z.index(n)
    print(z[p+1])

else:
"""
i = 1
while i <= m:
    p = (n * i) + 1
    if p not in z:
        print(i)
        break
    else:
        i += 1
