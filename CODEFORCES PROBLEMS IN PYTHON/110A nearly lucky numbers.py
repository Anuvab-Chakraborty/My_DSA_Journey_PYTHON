n=int(input())
n=str(n)
l=len(n)
z=0
for i in range(l):
    if n[i]=="4" or n[i]=="7":
        z+=1
if z==4 or z==7:
    print("YES")
else:print("NO")
