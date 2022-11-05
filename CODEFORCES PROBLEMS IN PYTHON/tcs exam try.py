n,k=map(int,input().split())
l=list(map(int,input().split()))
tower1=0
tower2=0
c=0
for i in range(n):
    tower1+=l[i]
    l.remove(l[i])
    if tower1>=k:
        tower2+=l[i]
        c+=1
        if tower2>=k:
            c+=1
            print(c)
        else:
            print(int("-1"))
            break
    else:
        print(int("-1"))
        break
        
