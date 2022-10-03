def prime_series(n):
    s=0
    z=n
    for i in range(1,n+1):
        if n%i==0:
            s+=1
    if s==2:
        return z

def armstrong_series(n):
    s=0
    temp=n
    while n>0:
        rem=n%10
        s=s+rem*rem*rem
        n=n//10
    if s==temp:
        return temp

def perfect_series(n):
    s=0
    p=n
    for i in range(1,n+1//2):
        if n%i==0:
            s+=i
    if s==p:
        return p

def fibo_series(n):
    if n <2:
        return n
    return (fibo_series(n-1)+fibo_series(n-2))

def palidnrome_number_series(n):
    rev=0
    p=n
    for i in range(n):
        while n>0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
    if rev==p:
        return p

def palindrome_string(n):
    if len(n)==0:
        return "Palindrome"
    elif n[0]!=n[-1]:
        return  "Not Palindrome"
    else:
        return palindrome_string(n[1:-1])


s="abva"
print(palindrome_string(s))
n=500
l=[]
#for i in range(0,n):
    #z=prime_series(i)
    #z=armstrong_series(i)
    #z=perfect_series(i)
    #p=fibo_series(i)
    #print(p)
    #z=palidnrome_number_series(i)
    #l.append(p)
    #if z!=None:
        #l.append(z)
#print(l)