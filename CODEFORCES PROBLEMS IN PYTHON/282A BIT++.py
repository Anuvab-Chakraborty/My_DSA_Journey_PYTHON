n=int(input())
x=0
for i in range(n):
    t=input()
    if(t[1]=='+'):
        x+=1
    else:
        x-=1
print(x)

"""
def bIT(l):
    count=0
    for i in l:
        for j in range(len(i)):
            if i[j]=="+":
                count+=0.5
            elif i[j]=="-":
                count-=0.5
    return int(count)

n=int(input())
l=[]
for i in range(n):
    m=input()
    l.append(m)
print(bIT(l))
"""