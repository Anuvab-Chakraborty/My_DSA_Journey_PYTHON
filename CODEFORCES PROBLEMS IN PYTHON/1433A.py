#1433A
def solve(n):
    l=[1,3,6,10]
    prev=((n%10)-1)*10
    current=l[len(str(n))-1]
    print(prev+current)
for _ in range(int(input())):
    n=int(input())
    solve(n)
