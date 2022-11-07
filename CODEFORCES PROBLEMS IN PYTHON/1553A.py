for _ in range (int(input())):
    n=int(input())
    if n%10==9:
        c=n//10 +1
        print(c)
    else:
        c=n//10
        print(c)