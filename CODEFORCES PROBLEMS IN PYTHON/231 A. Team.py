def team(z):
    count=0
    for i in z:
        if sum(i)>=2:
            count+=1
    return count

n=int(input())
l=[]
for i in range(n):
    m=list(map(int,input().split()))
    l+=[m]
#print(l)
print(team(l))