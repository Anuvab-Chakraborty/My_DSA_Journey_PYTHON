n=int(input())
l=sorted(list(map(int,input().split())))
l1=[];l2=[]
for i in l:
    if i%2==0:l1.append(i)
    else:l2.append(i)
if len(l1)==n//2 and len(l2)==n//2:
    print(0)
else:
    if len(l1)>len(l2):
        while True:
            l1.remove(l1[-1])
            if len(l2)==0:break
            l2.remove(l2[-1])
        print(sum(l1))
    else:
        while True:
            l2.remove(l2[-1])
            if len(l1)==0:break
            l1.remove(l1[-1])
        print(sum(l2))
