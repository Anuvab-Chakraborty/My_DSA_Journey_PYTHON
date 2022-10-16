s=input()
n=len(s)
cap=0
smal=0

for i in range(n):
    p=s[i]
    if p.islower():
        smal+=1
    else:
        cap+=1

if smal>=cap:
    print(s.lower())
else:
    print(s.upper())

#print(smal)
#print(cap)
