#1535B
from math import *
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    even=[];odd=[];ans=0
    for i in l:
        if i%2==0:even.append(i)
        else:odd.append(i)
    res=even+odd
    for i in range(n):
        for j in range(i+1,n):
            if gcd(res[i],2*res[j])>1:
                ans+=1
    print(ans)
