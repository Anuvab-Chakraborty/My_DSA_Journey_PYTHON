#1248B
n=int(input())
l=sorted(list(map(int,input().split())))
k=n//2
l1=l[0:k]
l2=l[k:]
z=sum(l1)**2+sum(l2)**2
print(z)
