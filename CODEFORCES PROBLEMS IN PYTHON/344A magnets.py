n=int(input())
l=[]
c=1
for i in range(n):
    m=input()
    l.append(m)
#print(l)
for i in range(n-1):
    if l[i][1]==l[i+1][0]:c+=1
print(c)