#432A
n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort()
c=0
f=0
for i in l:
    if i<=5-k:
        c+=1
if c>=3:
    f=c//3

print(f)
