#1760D
def solve(n,l):
    flag=0
    if n<=2:return "YES"
    for i in range(n-1):
        if l[i]==l[i+1]:pass
        elif l[i+1]-l[i]>0:flag=1
        elif l[i+1]-l[i]<0 and flag==1:return "NO"
    return "YES"
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(solve(n,l))
