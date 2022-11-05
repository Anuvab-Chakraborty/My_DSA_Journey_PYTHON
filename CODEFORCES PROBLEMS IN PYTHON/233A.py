#233A
n=int(input())
if n<1 or n%2!=0:print(-1)
else:
    l=[int(i) for i in range(1,n+1)]
    l=l[::-1]
    print(*l,end=" ")
        
