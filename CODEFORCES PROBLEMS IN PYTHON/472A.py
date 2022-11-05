#472A
def composite(n):
    flag=True
    primes=[2,3,7,11]
    for i in primes:
        if n%i==0 and n!=i:
            flag=False
    return flag
n=int(input())
for i in range(4,n):
    p=n-i
    if composite(i)==False and composite(p)==False:
        print(i,p)
        break
