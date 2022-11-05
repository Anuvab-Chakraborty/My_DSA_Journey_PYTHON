#1296A

def solve(a,b,c,n):
    m=max(max(a,b),c)
    a1=abs(m-a)
    b1=abs(m-b)
    c1=abs(m-c)
    f=a1+b1+c1
    z=n-f
    if z<0 or z%3!=0:
        print("NO")
    else:
        print("YES")



for _ in range(int(input())):
    a,b,c,n=map(int,input().split())
    solve(a,b,c,n)
