"""
b=[]
for i in range(5):
	a=input().split()
	b.append(a)
for i in range(5):
	for j in range(5):
		if b[i][j]=="1":
			g=abs(i-2)
			h=abs(j-2)
			k=g+h
print(k)
"""

"""
ans = 0
for i in range(5):
    s = input().split()
    for j in range(5):
        if int(s[j]) == 1:
            # print(i,j)
            ans = abs(i-2) + abs(j-2)
 
 
print(ans)
"""

"""
def main():
    matrix = []
    one = []
    for i in range(5):
        array = list(map(int, input().split()))
        for j in range(5):
            if array[j] == 1:
                one.append((i, j))
                break
    x1, y1 = one[-1]
    x2, y2 = 2, 2
    dist = abs(x1 - x2) + abs(y1 - y2)
    print(dist)
"""
