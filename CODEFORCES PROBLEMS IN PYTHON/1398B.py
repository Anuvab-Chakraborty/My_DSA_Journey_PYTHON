#1398B
"""
for _ in range(int(input())):
    l=list(input())
    c=0
    c2=0
    l1=[]
    i=0
    while i<len(l):
        if l[i]=="1" and l[i-1]==l[i]:
            c+=1
            i+=1
        elif l[i]=="1" and l[i-1]!=l[i]:
            c2+=1
            i+=1
            if c2>0:
                l1.append(c2)
        else:
            i+=1
    if c>0:
        l1.append(c)
    print(l1)
"""
for _ in range(int(input())):
    s=[len(i)for i in input().split('0')]
    s.sort(reverse=True)
    #print(s)
    print(sum(s[::2]))
