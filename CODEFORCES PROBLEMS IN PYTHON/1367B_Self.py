def solve(n,l):
    odd_count=0
    even_count=0
    for i in range(n):
        if i%2!=0 and l[i]%2==0:
            odd_count+=1
        elif i%2==0 and l[i]%2!=0:
            even_count+=1
    if odd_count==even_count:
        print(odd_count)
    elif odd_count!=even_count:
        print(-1)



for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    solve(n,l)
