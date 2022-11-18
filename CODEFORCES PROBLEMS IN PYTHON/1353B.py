#1353B
"""BRUTE FORCE BELOW
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if b[i]>a[i]:
            b[i],a[i]=a[i],b[i]
    print(sum(a))
"""
"""OPTIMIZED CODE"""
#1353B
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    while k>0:
        p=a.index(min(a))
        q=b.index(max(b))
        #print(p,q)
        if min(a)>=max(b):
            break
        else:
            a[p],b[q]=b[q],a[p]
        k-=1
    #print(a)
    print(sum(a))
