def watermelon(n):
    if n<=2:return "NO"
    elif n%2==0:
        return "YES"
    else:
        return "NO"
n=int(input())
print(watermelon(n))
