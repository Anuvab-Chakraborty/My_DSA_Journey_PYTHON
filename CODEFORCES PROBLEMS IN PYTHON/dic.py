"""
#def dictionary():
dic={'a':1,'c':5,'d':2}
print("dictionary:",dic)
#dic1=sorted(dic.items())
#print(dic1)
sorted_x = sorted(dic.items(), key=lambda kv: kv[1])
sorted_x=dict(sorted_x)
print(sorted_x)
z=max(sorted_x)
print(z)
"""
#top 2 most frequent char count
s="test string is he thing used here"
#s=s.replace(" ","")
s="".join(s.split())
print(s)

dc={}
l=[]
for i in s:
    if i not in dc:
        dc[i]=0
    dc[i]+=1
print(dc)
for i in dc:
    if dc[i]>1:
        print(i,dc[i])
        l.append(dc[i])
print(l)
summ=0
for i in l:
    summ+=i
print(summ)
#z=max(l)
#print(z)
#l.remove(z)
#print(l)
#z2=max(l)
#print(z2)

