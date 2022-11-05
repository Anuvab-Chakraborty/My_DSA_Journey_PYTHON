def bubble_sort(l):
    n=len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j]<l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

l=[-1,7,8,-7,-4]
z=(bubble_sort(l))
print(z)
