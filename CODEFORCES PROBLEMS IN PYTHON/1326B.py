#1326B
n=int(input())
l=list(map(int,input().split()))
s=0;l1=[];z=0
for i in range(n):
    z=l[i]+s
    l1.append(z)
    if l[i]>0:
        s+=l[i]
print(*l1)
