#1183B

for _ in range(int(input())):
    n,k=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    z=l[0]+k;ans=-1
    if l[-1]-z>k:print(ans)
    else:print(z)