#TDK
"""
from collections import Counter
s="abfcwbfbgbbwjhvvsudwiuhdfoihwfibiwsbs"
c=Counter(s)
print(c)
for key,value in c.items():
    if c[key]==1:
        print(key)
"""

"""
from datetime import datetime
start = datetime.now()
"""
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
    

n=86028122
z=sieve_original(n)

for _ in range(int(input())):
    p=int(input())
    print(z[p-1])
"""
end=datetime.now()
td = (end - start).total_seconds()
print(f"The time of execution of above program is : {td}ms")

"""
"""
#n=100000000
#print(len(sieve))

#limit=5000000
    #count=0
    #size=1
    #p=1

        if count==limit:
            size=p
            break
    print(size)
"""
