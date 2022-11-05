#9A
import math
m,n=map(int,input().split())
c_w=(6-max(m,n))+1
gc_d=math.gcd(c_w,6)
p=int(c_w/gc_d)
q=int(6/gc_d)
print(f"{p}/{q}")
