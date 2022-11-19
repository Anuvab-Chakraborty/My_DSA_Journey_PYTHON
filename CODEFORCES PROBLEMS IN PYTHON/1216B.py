#1216B
from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
d=defaultdict(list)
s=0
for index,value in enumerate(l):
    d[value].append(index+1)
l.sort(reverse=True)
for index,value in enumerate(l):
    s+=((value*index)+1)
#print(d)
print(s)
for i in sorted(d.keys(),reverse=True):
    print(*d[i],end=" ")