#490A
n=int(input())
l=list(map(int,input().split()))
one=[];two=[];three=[]
for index,value in enumerate(l):
    if value==1:
        one.append(index+1)
    elif value==2:
        two.append(index+1)
    elif value==3:
        three.append(index+1)
min_pairs=min(min(len(one),len(two)),len(three))
print(min_pairs)
for i,j,k in zip(one,two,three):
    print(i,j,k)
        
