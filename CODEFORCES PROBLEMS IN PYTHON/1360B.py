#1360B
def solve(n,l):
    l.sort()
    if n==2:
        print(abs(l[0]-l[1]))
    elif n==1:
        print(l[0])
    else:
        p=float("inf")
        for i in range(1,n):
            z=l[i]-l[i-1]
            z=abs(z)
            p=min(z,p)
        print(p)
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    solve(n,l)
