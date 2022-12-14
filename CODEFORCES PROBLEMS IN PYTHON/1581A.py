import math
for _ in range(int(input())):
    n=int(input())
    mod=1000000007
    z=(math.factorial(2*n)//2)%mod
    print(z)