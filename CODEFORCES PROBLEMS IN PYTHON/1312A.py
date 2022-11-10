#1312A
from math import *
def solve(m,n):
    p=gcd(m,n)
    q=min(m,n)
    if p==q:
        print("YES")
    else:print("NO")
for _ in range(int(input())):
    m,n=map(int,input().split())
    solve(m,n)
