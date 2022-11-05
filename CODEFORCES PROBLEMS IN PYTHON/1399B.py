#1399B

def solve(c,o,n):
    c_min=min(c)
    o_min=min(o)
    count=0
    for i in range(n):
        count+=max(c[i]-c_min,o[i]-o_min)
    print(count)


for _ in range(int(input())):
    n=int(input())
    candies=list(map(int,input().split()))
    orange=list(map(int,input().split()))
    solve(candies,orange,n)
