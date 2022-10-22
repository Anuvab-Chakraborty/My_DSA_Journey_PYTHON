#1409A
def solve(p,q):
    z=abs(p-q)
    ans=0   
    if z==0:
        return ans
        #break
    if z%10!=0:
        ans+=1
    ans+=z/10
    return int(ans)
        
        

    
n=int(input())
l=[]
for i in range(n):
    p,q=list(map(int,input().split()))
    print(solve(p,q))
