# 177A1
s = 0
n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        if j == i or j == (n - i - 1) or j == (n - 1) // 2 or i == (n - 1) // 2:
            s += l[j]

print(s)
