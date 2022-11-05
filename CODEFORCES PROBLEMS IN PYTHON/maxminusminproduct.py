def rev(s):
    l=[]
    s=s.lower()
    s=s.split()
    for i in s:
        l.append(i[::-1])
    s1=' '.join(l)
    #print(s1)
    s1=s1.title()
    #print(s1)
    return s1
rev("Hello World")

"""
arr=[1,5,6,9]
m1=min(arr)
m2=max(arr)
#print(m1,m2)
for i in range(len(arr)):
    arr[i]-=m2
    arr[i]*=m1

print(arr)
"""
