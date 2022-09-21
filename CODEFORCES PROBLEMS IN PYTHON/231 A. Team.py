def team(z):
    count=0
    #for i in z:
        #if sum(i)>=2:
            #count+=1
    if sum(z)>=2:count+=1
    return count

n=int(input())
#l=[]
z=0
for i in range(n):
    m=list(map(int,input().split()))
    z+=team(m)
    #l+=[m]
print(z)
#print(l)
#print(team(l))