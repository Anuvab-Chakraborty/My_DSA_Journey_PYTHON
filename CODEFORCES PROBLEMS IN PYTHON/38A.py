#38A
n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
#for i in range(1,n-1):
    #l[i]+=l[i-1]
#print(l)
z=a-1;x=b-1
s=sum(l[z:x])
print(s)
