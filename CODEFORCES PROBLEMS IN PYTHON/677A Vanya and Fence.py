m,n=list(map(int,input().split()))
z=list(map(int,input().split()))
#print(m,n,z)
w1=0
w2=0
for i in range(m):
    if z[i]<=n:
        w1+=1
    else:w2+=2
print(w1+w2)
