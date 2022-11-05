#1535A
def solve(l):
    k1=max(l[0],l[1])
    k2=max(l[2],l[3])
    z=abs(k2-k1)
    l.sort()
    p=l[-1]-l[-2]
    if p==z:
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    l=list(map(int,input().split()))
    solve(l)
