#202A
l=list(input())
l.sort()
c=""
s=l[-1]
for i in range(len(l)):
    if l[i]==s:
        c+=l[i]
print(c)
