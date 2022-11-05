#1520A

def solve(n,s):
    d={}
    d[s[0]]=1
    seen=s[0]
    for i in range(1,n):
        current=s[i]
        if current==seen:
            d[current]+=1
            seen=current
        else:
            if current in d.keys():
                if d[current]>0:
                    return "NO"
            else:
                d[current]=1
                seen=current
    return "YES"


for _ in range(int(input())):
    n=int(input())
    s=list(input())
    print(solve(n,s))
    #solve(n,s)
