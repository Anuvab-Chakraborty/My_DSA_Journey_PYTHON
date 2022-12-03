#n=int(input())
#l=[int(i) for i in range(1,n+1)]
l=[-1,0,3,5,9,12]
k=9
start=0;end=len(l)-1;mid=0;ans=-1
while end-start>=0:
    mid=start+ (end-start)//2
    #print(mid)
    if l[mid]==k:
        ans=mid
        break
    elif l[mid]<k:
        start=mid+1
        continue
    else:
        end=mid-1
        continue
print(ans)