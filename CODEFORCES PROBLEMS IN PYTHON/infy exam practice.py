def helper(x,y):
    while(y):
        x, y = y, x % y
     
    return x

def minTime(n,t,l):
    maxi  = max(t)
    ans=float("inf")
    val=0
    #l=t
    for i in range(len(l)):
        for j in range(1,maxi+1):
            l[i]=j
            gcd=helper(l[0],l[1])
            if gcd!=1:
                if ans<=gcd:
                    val=i
                ans=min(gcd,ans)
            for k in range(2,len(l)):
                gcd=helper(l[k],gcd)
                if gcd==1:
                    break
                else:
                    if ans<=gcd:
                        val=i
                    ans=min(gcd,ans)
        l[i]=t[i]
    #print(val,ans)
    #print(ans)
    t[val]=ans
    print(max(t))
    
def main():
    n=int(input())
    t=[];l=[]
    for i in range(n):
        p=int(input())
        t.append(p)
        l.append(p)
    res=minTime(n,t,l)
    #print(res)

if __name__=="__main__":
    main()
