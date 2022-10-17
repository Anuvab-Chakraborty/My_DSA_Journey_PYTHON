#734A
n=int(input())
s=input()
s=list(s)
c1=0
c2=0
for i in range(n):
    if s[i]=="D":c1+=1
    else:c2+=1
if c1>c2:print("Danik")
elif c2>c1:print("Anton")
else:print("Friendship")
