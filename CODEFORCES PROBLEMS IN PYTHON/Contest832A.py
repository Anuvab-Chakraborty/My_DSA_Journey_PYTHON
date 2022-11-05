"""
#832 CONTEST A
def solve(n,l):
    #l.sort()
    a=0
    b=0
    for i in l:
        if i>0:
            a+=i
        else:
            b+=i
    print(abs(a+b))


for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    solve(n,l)
"""
n=int(input())
s1="I hate it"
s2="I love it"
s3="I hate that"
s4="I love that"
for char in range(1, n + 1):
    if char%2==0 and char!=n:
        print(s4,end=" ")
    elif:
        print(s3,end=" ")
    if char==n:
        if char % 2==0:
            print(s2,end=" ")
        else:
            print(s1,end=" ")
        break
    
        
        
    
