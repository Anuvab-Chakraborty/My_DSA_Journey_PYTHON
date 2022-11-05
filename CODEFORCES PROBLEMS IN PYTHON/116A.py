n=int(input())
l=[]
for i in range(n):
    z=list(map(int,input().split()))
    l.append(z)

#print(l)
max_cur=float("-inf")
cur=sum(l[0])
if n<=2:
    print(cur)
else:
#print(cur)
    for i in range(1,n-1):
        left=cur-l[i][0]
        #print(left)
        new_cur=left+l[i][1]
        max_cur=max(max_cur,new_cur,cur)
        cur=new_cur
        #print(max_cur)
        #print(new_Cur)
    print(max_cur)
"""
10
0 5
1 7
10 8
5 3
0 5
3 3
8 8
0 6
10 1
9 0
"""
