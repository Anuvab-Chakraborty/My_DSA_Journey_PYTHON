s="aaa234bc@ sad$ hsadg^"
s=s.split(" ")
s="".join(s)
print(s)
c=0
n=len(s)
print(n)
for i in s:
    if i.isalpha() or i.isdigit():
        c+=1
print(c)
print(n-c)
