def petya(m,n):
    """
        #recursive method:

        if len(m)==0 and len(n)==0:return 0
        else:
            if ord(m[0])>ord(n[0]):return 1
            elif ord(m[0])==ord(n[0]):
                return petya(m[1::],n[1::])
            else:
                return -1
    """
    #using in-built lexigraphical methods:
    if m>n:return 1
    elif m==n:return 0
    else:return -1

m=input()
n=input()
m=m.lower()
n=n.lower()
print(petya(m,n))