#1676A
def solve(l):
    l1=l[:3]
    l2=l[3:]
    if sum(l1)==sum(l2):
        print("YES")
    else:print("NO")
    


for _ in range(int(input())):
    s=input()
    l=[int(i) for i in s]
    solve(l)
