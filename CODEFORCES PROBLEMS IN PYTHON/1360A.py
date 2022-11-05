#1360A
def solve(a,b):
    a1=max(a*2,b)
    b1=max(a,b*2)
    z=min(a1**2,b1**2)
    return z
for _ in range(int(int(input()))):
    a,b=map(int,input().split())
    print(solve(a,b))
