#1389A
for _ in range(int(input())):
    m,n=map(int,input())
    if m*2<=n:
        print(m,2*m)
    else:
        print(-1,-1)