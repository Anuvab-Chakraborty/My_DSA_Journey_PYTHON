#1619A
def solve(s):
    n=len(s)
    if n%2!=0:
        print("NO")
    else:
        p=n//2
        s1=s[:p]
        s2=s[p:]
        if s1==s2:
            print("YES")
        else:
            print("NO")

for _ in range(int(input())):
    s=input().lower()
    solve(s)
    
