for _ in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    #print(l)
    c=0
    for i in range(n-1):
        if l[i]<l[i+1]:c+=1
    #print(c)
    if c==n-1:print("YES")
    else:print("NO")
