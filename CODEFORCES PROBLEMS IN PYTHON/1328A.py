n=int(input())
for i in range(n):
    p,q=map(int,input().split())
    if p%q==0:
        print(0)
    else:
        print(abs(q-p%q))
