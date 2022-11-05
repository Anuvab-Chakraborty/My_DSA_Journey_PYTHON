def boy_Girl(s):
    a=set()
    for i in range(len(s)):
        if s[i] not in a:
            a.add(s[i])
        else:continue
    if (len(a))%2==0:
        print("CHAT WITH HER!")
    else:print("IGNORE HIM!")

    
s=input()
boy_Girl(s)
