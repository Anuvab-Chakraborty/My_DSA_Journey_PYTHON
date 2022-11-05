"""
n=int(input())
l=list(map(int,input().split()))
d={}
k=1
for i in l:
    d[i]=k
    k+=1
for i,j in d.items():
    print(d[j],end=' ')

"""

n=int(input())
l=list(map(int,input().split()))
#print(l)
l1=[]
dic={}
for index,value in enumerate(l):
        #print(index,value)
        if value not in dic:
                dic[value]=index+1
#print(dic)
          
for key,value in dic.items():
        print(dic[value],end=" ")
"""
We are basically searching the value in the dictionary first using k,v for
then we are finding the value associated to that value as a key in the dict
and appending that value in a list"""

