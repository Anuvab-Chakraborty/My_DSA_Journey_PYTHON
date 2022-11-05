def solve(x,y,n):
    """
    p=float("-inf")
    for i in range(n):
        k=i%x
        if k==y:
            p=max(p,i)
    print(p)
    """
    k=n%x
    if k<y:
        n=n-(k+abs(x-y))
        print(n)
    elif k==y:
        print(n)
    else:
        n=n-(abs(k-y))
        print(n)

t=int(input())
for i in range(t):
    x,y,n=map(int,input().split())
    solve(x,y,n)
