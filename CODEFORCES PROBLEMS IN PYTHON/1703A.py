#1703A
def solve(s):
    if s=="yes":
        return "YES"
    else:
        return "NO"
for _ in range(int(input())):
    s=input().lower()
    print(solve(s))
