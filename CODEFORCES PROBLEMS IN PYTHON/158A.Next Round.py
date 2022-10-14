def nextRound(z,n):
    count=0
    p=n-1
    for i in range(len(z)):
        if z[i]>=z[p] and z[i]>0:
            count+=1
    return count


m,n=list(map(int,input().split()))
z=list(map(int,input().split()))
print(nextRound(z,n))




"""
def nextRound(z,n):
    c=0
    for i in z:
        if i>=z[n-1] and i>0:
            c+=1
    return c
m,n=list(map(int,input().split()))
#print(m)
#print(n)

for i in range(m):
    z=list(map(int,input().split()))
    print(nextRound(z,n))
    break
"""