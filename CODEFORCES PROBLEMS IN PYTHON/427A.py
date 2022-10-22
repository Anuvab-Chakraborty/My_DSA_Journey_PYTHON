#427A
n=int(input())
l=list(map(int,input().split()))
ans=0
pol=0

for i in range(n):
    if l[i]>0:pol+=l[i]
    else:
        if pol>0:
            pol-=1
        else:ans+=1
print(ans)
