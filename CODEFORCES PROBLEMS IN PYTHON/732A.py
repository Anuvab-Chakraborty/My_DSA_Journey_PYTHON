m,n=list(map(int,input().split()))
i=1
while i<10:
    c=(m*i)%10
    if c==0 or c==n:
        print(i)
        break
    i+=1
