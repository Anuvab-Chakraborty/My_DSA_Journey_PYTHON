#1624A
def solve(n,l):
    if n==1:
        return 0
    z=max(l)-min(l)
    return z
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(solve(n,l))
