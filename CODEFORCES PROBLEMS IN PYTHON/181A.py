#181A
n,m = map(int, input().split())
x,y = 0,0
for i in range(n):
    line = input()
    for j in range(m):
        if line[j] == "*":
            x^=i
            y^=j
print(x+1,y+1)
