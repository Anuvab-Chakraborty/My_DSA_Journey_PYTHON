#92A
n,m=map(int,input().split())
i=1
p=m
while True:
    flag=True
    for i in range(1,n+1):
        if p>=i:
            p-=i
        else:
            flag=False
            break
    if flag==False:
        break
print(p)
