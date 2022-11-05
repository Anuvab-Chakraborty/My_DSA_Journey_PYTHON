#1472B
from collections import Counter
def solve(n,l):
    dic=Counter(l)
    if dic[1]%2==0 and dic[2]%2==0:
        print("YES")
    elif dic[1]%2==0 and dic[1]>=2:
        print("YES")
    else:print("NO")
    
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    solve(n,l)
