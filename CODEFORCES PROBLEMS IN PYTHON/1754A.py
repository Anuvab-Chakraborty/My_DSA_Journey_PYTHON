#1754A
for _ in range(int(input())):
    n=int(input())
    l=input()
    ans=0
    for i in range(n):
        if l[i]=="Q":ans+=1
        else:ans-=1
        if ans<0:ans=0
    if ans>0:print("NO")
    else:print("YES")