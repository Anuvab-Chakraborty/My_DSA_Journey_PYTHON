n=int(input())
l=list(map(int,input().split()))
c=0

mini=l[::-1].index(min(l))
#print(mini)
maxi=l.index(max(l))
#print(maxi)
c=maxi+mini
if maxi<=n-mini-1:
    print(c-1)
elif maxi>=n-mini-1:
    print(c)
else : print(0)
"""
if c>=n:
    print(c-1)
else:
    print(c)
"""
