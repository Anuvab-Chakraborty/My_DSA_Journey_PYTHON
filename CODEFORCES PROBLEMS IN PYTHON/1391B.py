#1391B
for _ in range(int(input())):
    c=0
    m,n=map(int,input().split())
    for i in range(m):
        l=input()
        for j in range(len(l)):
            if (j==len(l)-1 and l[j]=="R") or (i==m-1 and l[j]=="D"):
                c+=1
    print(c)
