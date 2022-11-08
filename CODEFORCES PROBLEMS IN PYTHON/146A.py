# 146A
m = int(input())
n = list(input())
p1 = n.count("4")
p2 = n.count("7")
if p1 + p2 == m:
    p = m // 2
    s1 = [int(n[i]) for i in range(p)]
    # print(s1)
    s2 = [int(n[i]) for i in range(p, m)]
    # print(s2)
    s1_s = sum(s1)
    # print(s1_s)
    s2_s = sum(s2)
    # print(s2_s)
    if s1_s == s2_s:
        print("YES")
    else:
        print("NO")
else:
    print("NO")