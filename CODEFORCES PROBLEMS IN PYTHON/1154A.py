#1154A
Li=list(map(int, input().split()))
s=max(Li)
Li.sort()
a= s - Li[0]
b= s - Li[1]
c= s - Li[2]
print(a,b,c)
