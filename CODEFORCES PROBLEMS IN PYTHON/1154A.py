#1154A
l=list(map(int,input().split()))
s=max(l)
l.sort()
a=s-l[0]
b=s-l[1]
c=s-l[2]
print(a,b,c)
