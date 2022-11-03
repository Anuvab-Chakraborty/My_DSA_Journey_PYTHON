#1311A
for _ in range(int(input())):
    a,b=map(int,input().split())
    if abs(b-a)%2==0:
        print(min(abs(b-a),1+(b-a>0)))
    else:
        print(1+(a-b>0))
