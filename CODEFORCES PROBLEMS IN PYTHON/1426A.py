#1426A
from math import *

def solve(n,x):
    c=1
    if n<=2:
        print(c)
    else:
        n-=2
        z=ceil(n/x)
        c+=z
        print(c)
        



for _ in range(int(input())):
    n,x=map(int,input().split())
    solve(n,x)
