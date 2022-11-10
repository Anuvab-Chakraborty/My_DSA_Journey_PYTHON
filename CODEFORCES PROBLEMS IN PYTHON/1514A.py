#1514A
from math import *
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        z=int(sqrt(l[i]))
        if z*z!=l[i]:
            print("YES")
            break
    else:
        print("NO")
