def way_too_long_words(n):
    if len(n)<=10:
        return n
    else:
        l=[]
        l.append(n[0])
        z=n[1:-1]
        l.append(str(len(z)))
        l.append(n[-1])
        return "".join(l)

n=int(input())
for i in range(n):
    z=input()
    print(way_too_long_words(z))