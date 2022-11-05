def solve(l):
    s=0
    d=0
    for i in range(len(l)):
       if i%2!=0:
           p=max(l[0],l[-1])
           s+=p
           l.remove(p)
       else:
           q=max(l[0],l[-1])
           d+=q
           l.remove(q)
    print(d,s)


n=int(input())
l=list(map(int,input().split()))
solve(l)
