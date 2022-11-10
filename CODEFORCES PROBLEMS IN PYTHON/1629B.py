# 1629B
for _ in range(int(input())):
    l, r, k = map(int, input().split())
    if l == r:
        if l == 1:
            print("NO")
        else:
            print("YES")
    else:
        if (r - l + 1) % 2 == 0:
            z = (r - l + 1) // 2
        else:
            if l % 2 == 0:
                z = ((r - l + 1)) // 2
            elif l % 2 != 0:
                z = ((r - l)) // 2 + 1
        if k >= z:
            print("YES")
        else:
            print("NO")

