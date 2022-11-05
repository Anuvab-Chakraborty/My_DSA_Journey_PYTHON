#431A

l=list(map(int,input().split()))
s=input()
z=0
for i in s:
    j=int(i)
    z+=l[j-1]
print(z)
