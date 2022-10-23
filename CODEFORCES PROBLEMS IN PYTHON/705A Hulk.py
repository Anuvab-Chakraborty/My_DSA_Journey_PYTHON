n=int(input())
s1="I hate it"
s2="I love it"
s3="I hate that"
s4="I love that"
for char in range(1, n + 1):
    if char==n:
        if char % 2==0:
            print(s2,end=" ")
        else:
            print(s1,end=" ")
        break
    if char%2==0:
        print(s4,end=" ")
    else:
        print(s3,end=" ")