for _ in range(int(input())):
    n=int(input())
    """
    z=(n//2)+1
    p=(2**z)-2
    print(p)
    """
    p=2**n
    l=p+2*(2**(((n//2)-1))-1)
    print(l)
    r=(2**(n//2))*(2**((n//2)-1))
    print(r)
    print(l-r)
    
