"""
se=set(list(map(int,input().split())))
print(4-len(se))

"""
l=list(map(int,input().split()))
a=set()
for i in l:
    if i not in a:
        a.add(i)
m=len(a)
print(4-m)
