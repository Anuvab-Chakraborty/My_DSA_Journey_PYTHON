def solve(n):
    if n < 31:
        print("NO")
    else:
        print("YES")
        a = 6;
        b = 10;
        c = 15;
        z = 31
        if n == 36 or n == 44 or n == 40:
            print(a, b, c, n - z)
        else:
            print(a, b, c - 1, n - (z - 1))


for _ in range(int(input())):
    n = int(input())
    solve(n)