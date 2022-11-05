#80A
from math import *
def sieve_original(n):
    
    l=[]
    sieve=[True]*(n+1)
    sieve[0]=False
    sieve[1]=False
    for i in range(2,int(sqrt(n))+1):
        if sieve[i]==True:
            for j in range(i*i,n+1,i):
                sieve[j]=False
    for p in range(2,len(sieve)):
        if sieve[p]==True:
            l.append(p)
    return l
l=sieve_original(500)
#print(l)
m,n=map(int,input().split())
if n in l:
    z=l.index(n)
    p=l.index(m)
    f=z-p
    if f==1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
