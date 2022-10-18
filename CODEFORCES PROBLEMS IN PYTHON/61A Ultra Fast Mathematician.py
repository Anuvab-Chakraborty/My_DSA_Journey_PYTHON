num1=input()
num2=input()
l=[]
if abs(int(num1[0])-int(num2[0]))==0:
    l.append("0")
    for i in range(1,len(num1)):
        if num1[i]!=num2[i]:
            l.append("1")
        else:
            l.append("0")
else:
    for i in range(len(num1)):
        if num1[i]!=num2[i]:
            l.append("1")
        else:
            l.append("0")
l=("".join(l))
print(l)

