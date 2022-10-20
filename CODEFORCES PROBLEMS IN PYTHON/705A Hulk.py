n=int(input())
s1="I hate it"
s2="I love it"
s3="I hate that"
s4="I love that"
for i in range(1,n+1):
    if i==n:
        if i % 2==0:
            print(s2,end=" ")
        else:
            print(s1,end=" ")
        break
    if i%2==0:
        print(s4,end=" ")
    else:
        print(s3,end=" ")