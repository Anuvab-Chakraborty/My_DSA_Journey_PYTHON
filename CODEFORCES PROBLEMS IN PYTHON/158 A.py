def nextRound(z,n):
    count=0
    p=n-1
    for i in range(len(z)):
        if z[i]>=z[p] and z[i]>0:
            count+=1
    return count


m,n=list(map(int,input().split()))
#for i in range(m):
z=list(map(int,input().split()))
#print(z)   
print(nextRound(z,n))
