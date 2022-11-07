#822A
m,n=sorted(map(int,input().split()))
s=1
for i in range(1,m+1):
    s*=i
print(s)
