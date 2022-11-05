#707A
def solve(l):
    for i in l:
        if i=="C" or i=="M" or i=="Y":
            return "#Color"
    return "#Black&White"
l=[]
m,n=map(int,input().split())
for _ in range(m):
    s=input().split()
    l+=s
#print(l)
print(solve(l))
