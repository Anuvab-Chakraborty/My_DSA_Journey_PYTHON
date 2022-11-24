n,d=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(n):
        if i==j:pass
        else:
            if abs(l[i]-l[j])<=d:c+=1
print(c)