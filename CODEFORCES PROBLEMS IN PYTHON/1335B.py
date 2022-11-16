#1335B
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    s=""
    i=65
    p=90
    s_a=""
    while i<=p:
        s_a+=chr(i)
        i+=1
    s_b=s_a[:b]
    if a%b==0:
        a_s=s_b*(int(a/b))
    else:
        r=a%b
        a_s=s_b*(int(a//b))+s_b[:r]
    if n%a==0:
        s=a_s*(int(n/a))
    else:
        r2=n%a
        s=a_s*(int(n//a))+a_s[:r2]
    print(s.lower())
