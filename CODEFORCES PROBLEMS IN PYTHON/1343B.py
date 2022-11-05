#1343B
def solve(m):
    if (m//2)%2!=0:
        print("NO")
    else:
        print("YES")
        even=0
        odd=0
        for i in range(2,m+1,2):
            print(i,end=" ")
            even+=i
        for i in range(1,m-2,2):
            print(i,end=" ")
            odd+=i
        print(even-odd)
n=int(input())
for i in range(n):
    m=int(input())
    solve(m)
