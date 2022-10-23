n=int(input())
Li=list(map(int, input().split()))
mini= Li[::-1].index(min(Li))
maxi=Li.index(max(Li))
#"""
if maxi+mini>=n:
    print(mini+maxi-1)
else:print(mini+maxi)
#"""
"""
if maxi<n-mini-1:
    print(maxi+mini)
elif maxi>n-mini-1:
    print(maxi+mini-1)
else:
    print(0)
"""