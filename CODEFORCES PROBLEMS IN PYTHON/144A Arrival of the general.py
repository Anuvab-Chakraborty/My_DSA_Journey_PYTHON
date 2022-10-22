n=int(input())
l=list(map(int,input().split()))
mini=l[::-1].index(min(l))
maxi=l.index(max(l))
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