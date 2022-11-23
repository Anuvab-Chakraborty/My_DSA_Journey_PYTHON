n=int(input())
l=list(map(int,input().split()))
a=1;b=n;c=0;z=float("inf")
if abs(l[0]-l[-1])<=z:
    z=abs(l[0]-l[-1])
for i in range(n-1):
    if abs(l[i]-l[i+1])<=z:
        z=abs(l[i]-l[i+1])
        a=i+1;b=i+2
print(a,b)