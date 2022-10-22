#510A
m,n=list(map(int,input().split()))

for i in range(1,m+1):
    if i%2 == 0:
        if i%4!=0:
            for j in range(1,n):
                print(".",end="")
            print("#")
        else:
            print("#",end= "") 
            for j in range(1,n):
                print(".",end= "")
            print()
    else:
        for j in range(n):
            print("#",end="")
        print()
"""
n,m = map(int,input().split( ))
for i in range(n):
    if i%2==0:
        print('#'*m)
    elif i%4==1:
        print('.'*(m-1)+'#')
    else:
        print('#'+'.'*(m-1)
"""
"""
n, m = [int(i) for i in input().split()]
ho = "#"
hi = "."
for i in range(1, n  + 1):
    if i % 4 != 0 and i % 2 == 0:
        print(hi*(m-1) + ho)
    elif i % 4 == 0:
        print(ho + hi* (m - 1))
    else:
        print(ho * m)
"""
