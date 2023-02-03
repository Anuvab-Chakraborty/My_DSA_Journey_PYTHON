#721A
n=int(input())
l1=list(input().split("W"))
l2=[];c=0
for i in l1:
    if i!="":l2.append(len(i));c+=1
print(c)
print(*l2)
