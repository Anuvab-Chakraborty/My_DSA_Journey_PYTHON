def cap(s):
    p=s[0].upper()
    q=s[1::]
    r=p+q
    return r
s=input()
print(cap(s))