#1337B
"""
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    for _ in range(y):
        x=min(x,x//2+10)
    x-=(10*z)
    if x>0:print("NO")
    else:print("YES")
"""
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    while y>0 and x>20:
        x=(x//2)+10
        y-=1
    final=x-(10*z)
    if final>0:print("NO")
    else:print("YES")
