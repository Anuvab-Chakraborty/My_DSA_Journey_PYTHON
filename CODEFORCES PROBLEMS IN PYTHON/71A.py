def waytoolong(l):
    n=len(l)
    z=[]
    if n<=10:
        return l
    else:
        start=l[0]
        z.append(start)
        end=l[-1]
        middle=l[1:-1]
        mid_len=str(len(middle))
        z.append(mid_len)
        z.append(end)
        #final=start+mid_len+end
        #return final
        return "".join(z)




n=int(input())
for i in range(n):
    l=input()
    print(waytoolong(l))
    
