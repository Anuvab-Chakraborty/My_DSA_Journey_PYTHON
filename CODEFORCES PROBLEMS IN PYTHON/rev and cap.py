def rev(s):
    s=s.lower()
    s=s.split()
    l=[]
    for i in s:
        i=i[::-1]
        #print(i)
        l.append(i)
    #print(l)
    del s
    s=" ".join(l)
    #print(s)
    s=s.title()
    return s
s=input()
#s="Anuvab Chakraborty is my name"
print(rev(s))

