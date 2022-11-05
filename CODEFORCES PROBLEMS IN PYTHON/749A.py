#749A
#"""
from math import *
def prime(n):
    c=0
    primes=[True]*(n+1)
    primes[0]=False
    primes[1]=False
    for p in range(2,int(sqrt(n))+1):
        if primes[p]==True:
            for i in range(p*p,n+1,p):
                primes[i]=False
    print(primes)
    for i in range(len(primes)):
        if primes[i]==True:
            c+=1
    print(c)
,

n=int(input())
prime(n)
"""
n=int(input())
if n%2==0:
    a=n//2
    print(a)
    print("2 "*a)
else:
    a=(n-1)//2
    print(a)
    print("2 "*(a-1),end="")
    print("3")
"""
