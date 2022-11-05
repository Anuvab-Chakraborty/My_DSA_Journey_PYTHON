#1512A

def solve(n,l):
    for i in range(m):
        if l.count(l[i])==1:
            print(i+1)

p=int(input())
for i in range(p):
    m=int(input())
    l=list(map(int,input().split()))
    solve(m,l)
"""
l=[1,2,3,57,62,4]
z=l[:3]
print(z)
"""
