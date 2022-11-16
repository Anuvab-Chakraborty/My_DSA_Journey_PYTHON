# 1583A
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


a = 50000
z = sieve_original(a)

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = 0
    if sum(l) in z:
        for i in range(n):
            if l[i] % 2 != 0:
                m = i + 1

    if m == 0:
        print(n)
        l1 = [int(i) for i in range(1, n + 1)]
        print(*l1)
    else:
        print(n - 1)
        for i in range(1, n + 1):
            if i == m:
                pass
            else:
                print(i, end=" ")
        print()
