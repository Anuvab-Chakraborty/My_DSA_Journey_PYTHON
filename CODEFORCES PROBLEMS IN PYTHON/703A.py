#703A
n=int(input())
c=0
c2=0
for i in range(n):
    m,n=(map(int,input().split()))
    if m>n:
        c+=1
    elif m<n:
        c2+=1
    else:
        continue
if c>c2:
    print("Mishka")
elif c==c2:
    print("Friendship is magic!^^")
else:
    print("Chris")
