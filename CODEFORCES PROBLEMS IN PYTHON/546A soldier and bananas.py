#546A
def sol_ban(k,n,w):
    s = 0
    for i in range(w + 1):
        s += k * i
    # print(s)
    z = n - s
    if z > 0:
        i = 0
        print(i)
    else:
        print(abs(z))
k,n,w=list(map(int,input().split()))
sol_ban(k,n,w)
"""
for i in range(w+1):
    s+=k*i
#print(s)
z=n-s
if z>0:
    i=0
    print(i)
else:print(abs(z))
"""