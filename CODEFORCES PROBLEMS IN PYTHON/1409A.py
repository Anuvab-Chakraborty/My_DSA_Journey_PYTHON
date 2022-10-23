#1409A
def solve(p,q):
    diff=abs(p-q)
    ans=0   
    if diff==0:
        return ans
        #break
    if diff%10!=0:
        ans+=1
    ans+=diff/10
    return int(ans)
        
        

    
n=int(input())
l=[]
for i in range(n):
    p,q=list(map(int,input().split()))
    print(solve(p,q))
