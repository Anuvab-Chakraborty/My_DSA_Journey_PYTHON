#32B
s=input()
z=""
i=0
while i<len(s):
    if s[i]==".":
        z+="0"
        i+=1
    elif s[i]=="-":
        if s[i+1]==".":
            z+="1"
            i+=2
        else:
            z+="2"
            i+=2
        
print(z)
        
        
