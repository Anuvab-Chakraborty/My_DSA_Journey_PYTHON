#785A
d={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
n=int(input())
l=[]
for i in range(n):
    z=list(map(str,input().split()))
    l+=z
#print(l)
s=0
for i in l:
    if i in d.keys():
        s+=d[i]
print(s)
"""
for key,value in d.items():
    for i in l:
        if i==key:
            s+=value
print(s)
"""
