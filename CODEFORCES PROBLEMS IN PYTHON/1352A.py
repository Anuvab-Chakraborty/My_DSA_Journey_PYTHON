#1352A
def solve(m):
    l=[]
    i=0
    while m>0:
        c=m%10
        m=m//10
        if c!=0:
            l.append(c*(10**i))
        i+=1
    print(len(l))
    for i in l:
        print(i,end=" ")
    print()
            

n=int(input())
for i in range(n):
    m=int(input())
    solve(m)
