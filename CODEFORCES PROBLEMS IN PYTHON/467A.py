n=int(input())
l=[]
for i in range(n):
    z=list(map(int,input().split()))
    l.append(z)
c=0
#print(l)
for i in l:
    z=i[1]-i[0]
    if z>=2:c+=1
print(c)
