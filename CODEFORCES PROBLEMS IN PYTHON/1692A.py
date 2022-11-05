#1692A
def solve(l):
    a=l[0]
    l.sort()
    p=l.index(a)
    print(3-p)

    
for _ in range(int(input())):
    l=list(map(int,input().split()))
    solve(l)
