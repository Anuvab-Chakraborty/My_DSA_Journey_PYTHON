#492A
n=int(input())
z=0
p=float("-inf")
if n==1:
    print(1)
else:
    for i in range(n):
        z+=(i*(i+1))//2
        if z<=n:
            p=max(p,i)
    print(p)
