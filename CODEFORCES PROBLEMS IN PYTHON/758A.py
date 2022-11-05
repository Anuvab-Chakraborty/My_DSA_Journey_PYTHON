#758A
n=int(input())
l=list(map(int,input().split()))
c=0
z=max(l)
if n==1:
    print(c)
else:
    for i in range(n):
        c+=z-l[i]
    print(c)
