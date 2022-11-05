#734B
condition=True
c=0
k2,k3,k5,k6=map(int,input().split())
while condition:
    if k2>=1 and k5>=1 and k6>=1:
        c+=256
        k2-=1
        k5-=1
        k6-=1
    elif k2>=1 and k3>=1:
        c+=32
        k2-=1
        k3-=1
    else:
        condition=False
print(c)
