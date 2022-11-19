#1206B
n=int(input())
l=list(map(int,input().split()))
s_min=0;s_max=0;cnt_max=0;cnt_min=0;cnt_z=0;ans=0
for i in range(n):
    if l[i]>=1:
        s_max+=l[i]
        cnt_max+=1
    elif l[i]<=-1:
        s_min+=l[i]
        cnt_min+=1
    elif l[i]==0:cnt_z+=1
final1=abs(s_min)-cnt_min
final2=s_max-cnt_max
if cnt_min%2!=0:
    if cnt_z>0:
        ans+=1
        cnt_z-=1
    else:ans+=2
#print(final1)
#print(final2)
ans+=final1+final2+cnt_z
print(ans)
