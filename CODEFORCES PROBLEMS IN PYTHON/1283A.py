#1283A
def solve(l):
    z=((24-int(l[0]))*60)-int(l[1])
    print(z)

for _ in range(int(input())):
    l=list(map(str,input().split()))
    #print(z)
    solve(l)
