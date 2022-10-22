#141A
from collections import Counter
s1=input().lower()
s2=input().lower()
s=input().lower()
s_fin=s1+s2
"""
d={}
if len(s)!=len(s_fin):
    print("NO")
else:
    for i in range(len(s)):
        if i not in dic

"""
if Counter(s_fin)==Counter(s):
    print("YES")
else:
    print("NO")
