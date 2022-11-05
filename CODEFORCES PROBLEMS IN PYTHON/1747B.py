#1747B
def solve(n):
    if n%2==0:
        print(n//2)
        for i in range(n//2):
            print(i*3+1,n*3-i*3)
    else:
        print((n//2)+1)
        for i in range(n//2+1):
            print(i*3+1,n*3-i*3)
for _ in range(int(input())):
    n=int(input())
    solve(n)
