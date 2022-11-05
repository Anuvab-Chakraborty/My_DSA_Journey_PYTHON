#214A
m,n=map(int,input().split())
p=max(m,n)
c=0
for a in range(p+1):
    for b in range(p+1):
        if (a**2)+b==n and (b**2)+a==m:c+=1
print(c)
