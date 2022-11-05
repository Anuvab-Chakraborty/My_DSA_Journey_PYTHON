#1472A
def solve(h,w,n):
    c=1
    while h%2==0:
        c*=2
        h=h//2
    while w%2==0:
        c*=2
        w=w//2
    if c>=n:
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    h,w,n=map(int,input().split())
    solve(h,w,n)
