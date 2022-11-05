#1551A
"""
for i in range(int(input())):
    n = int(input())
    if n==2:
        print(0,1)
    elif n== 1:
        print(1,0)
    elif n % 3 == 0:
        print(n//3,n//3)
    elif n%3 == 2:
        print((n-2) //3, (n-2)//3 +1)
    else:
        print(((n-1) //3)+1, (n-1)//3)


"""

import math
def solve(n):
    x=n//3
    y=math.ceil((n-x)/2)
    if x+2*y==n:
        print(x,y)
    else:
        print(y,x)


for _ in range(int(input())):
    n=int(input())
    solve(n)

