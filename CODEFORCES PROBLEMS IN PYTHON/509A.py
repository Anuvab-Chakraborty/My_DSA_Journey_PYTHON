n=int(input())
l=[[1]*n]
for i in range(n):
    l1=[1]+[0]*(n-1)
    l+=[l1]
#print(l)
for i in range(n):
    for j in range(1,n):
        l[i][j]=l[i][j-1]+l[i-1][j]
print(l[n-1][n-1])
