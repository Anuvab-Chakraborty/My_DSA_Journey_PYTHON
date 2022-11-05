#1371A
def solve(n):
    if n<3:
        return 1
    elif n%2==0:
        return n//2
    else:
        return (n+1)//2
for _ in range(int(input())):
    n=int(input())
    print(solve(n))
