def final_count(s):
    n=len(s)
    count=0
    for i in range(n-1):
        if s[i]==s[i+1]:
            count+=1
    return count


n=int(input())
s=input()
print(final_count(s))