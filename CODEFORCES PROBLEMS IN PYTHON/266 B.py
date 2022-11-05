n,m=list(map(int,input().split()))
s=input()
s=list(s)
for i in range(m):
    j=0
    while j<n-1:
        if s[j]=="B" and s[j+1]=="G":
            s[j],s[j+1]=s[j+1],s[j]
            j+=1
        j+=1
print("".join(s))
