#sqrt prime:
import math 

def solve(n):
    if n<2:
        return "non prime"
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return "non prime"
    return "prime"



n=2500
for i in range(n+1):
    print(i,solve(i))
#for 1-n->10^6 TC:O(N)
#for 1-sqrt(n) -> 10^3 TC:O(sqrt(N))
