n=int(input())
l=list(map(int,input().split()))
z=list(map(int,input().split()))
a=set()
for i in range(1,l[0]+1):
    a.add(l[i])
for i in range(1,z[0]+1):
    a.add(z[i])
#print(a)
if len(a)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
