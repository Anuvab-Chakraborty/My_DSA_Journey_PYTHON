m,n=list(map(int,input().split()))
p=240
c=0
for i in range(1,m+1):
    n+=5*i
    if n<=p:
        c+=1
    
print(c)
