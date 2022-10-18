n=int(input())
dic={}
l=list(map(int,input().split()))
for index,value in enumerate(l):
    if value not in dic:
        dic[value]=index+1
#print(dic)
for keys,value in dic.items():
    print(dic[value],end=" ")