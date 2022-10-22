#1335A
n=int(input())
l=[]
for i in range(n):
    z=int(input())
    l.append(z)
for i in l:
    if i%2==0:
        print((i//2)-1)
    else:
        print(i//2)
