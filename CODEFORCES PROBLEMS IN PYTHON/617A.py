#617A

def elephant_friend(n,c):
    if n%5!=0:
        c+=1
    c+=n//5
    return c

n=int(input())
c=0
print(elephant_friend(n,c))
    
