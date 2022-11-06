#1351B
for _ in range(int(input())):
    """
    a1,b1=sorted(map(int,input().split()))
    a2,b2=sorted(map(int,input().split()))
    """
    a1,b1=map(int,input().split())
    a2,b2=map(int,input().split())
    if max(a1,b1)==max(a2,b2):
        z=max(a1,b1)
        if min(a1,b1)+ min(a2,b2)==z:
            print("YES")
        else:print("NO")
    else:print("NO")
    """
    if a1+a2==b1==b2:
        print("YES")
    else:
        print("NO")
    """
