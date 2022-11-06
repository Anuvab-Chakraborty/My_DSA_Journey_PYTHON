def solve(n):
    c2=0
    c3=0
    if n<=1:
        return 0
    else:
        while True:
            while n%2==0:n//=2;c2+=1
            while n%3==0:n//=3;c3+=1
            if n>1 or c2>c3:
                return -1
            else:
                z=(2*c3)-c2
                return z

for _ in range(int(input())):
    n=int(input())
    z=solve(n)
    print(z)