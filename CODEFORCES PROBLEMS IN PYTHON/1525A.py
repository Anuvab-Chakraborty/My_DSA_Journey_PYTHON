# 1525A
from math import *


def solve(n):
    w = 100 - n
    p = gcd(w, n)
    if p == 1:
        print(100)
    else:
        print(w // p + n // p)


for _ in range(int(input())):
    n = int(input())
    solve(n)
