def team(l):
    total=0
    count=0
    for i in l:
        total=sum(i)
        if total>=2:
           count+=1
    return count


n=int(input())
l=[]
for i in range(n):
    m=list(map(int,input().split()))
    l.append(m)
print(team(l))
