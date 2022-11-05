#1520B
for _ in range(int(input())):
    n=int(input())
    count,temp=0,n
    while(n>0):
        n//=10
        count+=1
    t=int('1'*count)
    print(9*(count-1)+temp//t)
    
