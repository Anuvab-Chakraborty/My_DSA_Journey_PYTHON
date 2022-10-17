def final_(n):
    a=set()
    for i in str(n):
        if i in a:
            return False
        a.add(i)
    return True

n=int(input())
while True:
    n+=1
    if final_(n):
        print(n)
        break
"""
n=n+1
while len(set(str(n)))<4:n+=1
print(n)
"""
