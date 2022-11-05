#1367A
for _ in range(int(input())):
    s=input()
    output=""
    n=len(s)
    for i in range(0,n-2,2):
        output+=s[i]
    output+=s[-2:]
    print(output)
