#148A
k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
a=set()
l1=[i for i in range(1,d+1)]
#print(l)
for i in l1:
    if i%k==0 or i%l==0 or i%m==0 or i%n==0:
        if i not in a:
            a.add(i)
print(len(a))
