#1658B
mod=998244353
def fact(n):
    if n==0:return 1
    else:
        return ((n%mod)*(fact(n-1)%mod))%mod



for _ in range(int(input())):
    n=int(input())
    if n%2!=0:print(0)
    else:
        ans=(fact(n//2)*fact(n//2))%mod
        print(ans)
