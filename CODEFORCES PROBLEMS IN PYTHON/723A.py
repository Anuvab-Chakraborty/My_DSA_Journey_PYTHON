l=list(map(int,input().split()))
l.sort()
s=(l[1]-l[0])+(l[-1]-l[1])
print(s)
