#49A
n=input().split(" ")
n="".join(n)
n=n.lower()
#print(n)
z=n[-2]
if z=="a" or z=="e" or z=="i" or z=="o" or z=="u" or z=="y":
    print("YES")
else:print("NO")