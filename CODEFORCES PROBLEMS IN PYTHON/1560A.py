#1560A

def solve():
    m=int(input())
    i=1
    count=0
    while 1:
        if i%3!=0 and i%10!=3:
            count+=1
        if count==m:
            print(i)
            break
        i+=1


n=int(input())
for i in range(n):
    solve()
