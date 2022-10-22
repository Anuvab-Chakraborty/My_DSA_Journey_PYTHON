n=int(input())
l=list(map(int,input().split()))
c=0
maxi=l[0]
mini=l[0]
for i in range(1,n):
    maxi=max(maxi,l[i-1])
    mini=min(mini,l[i-1])
    if l[i]<mini or l[i]>maxi:
        c+=1
print(c)     
