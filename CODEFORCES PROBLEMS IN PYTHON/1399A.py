#1399A
def solve(m,l):
    i=1
    l.sort()
    flag=True
    while i<m:
        if abs(l[i]-l[i-1])<=1:
            i+=1
            continue
        else:
            flag=False
            break
    if len(l)==1:print("YES")
    elif flag:print("YES")
    else:print("NO")

    
n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    solve(m,l)

