n=int(input())
count=0
first_=[]
second_=[]
for i in range(n):
    z=list(map(int,input().split()))
    first_.append(z[0])
    second_.append(z[1])
for i in first_:
    for j in second_:
        if i==j:
            count+=1
print(count)
