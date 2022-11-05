"""
s="my name is anuvab"
s="".join(s.split())
print(s)
set1=set()
for i in s:
    if i not in set1:
        set1.add(i)
s1=list(set1)
print(s1)
s1="".join(s1)
print(s1)
"""
s="my name is anuvab"
s="".join(s.split())
print(s)
dc={}
for i in s:
    if i not in dc:
        dc[i]=0
    dc[i]+=1
print(dc)
#print the alphabet with most repitation
max1=float("-inf")
for key,values in dc.items():
    max1=max(max1,values)
print(max1)
