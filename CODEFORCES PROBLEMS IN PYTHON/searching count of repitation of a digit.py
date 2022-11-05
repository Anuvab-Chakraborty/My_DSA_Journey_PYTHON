from collections import Counter
num=123228
toSearch="2"
num=str(num)
dic=Counter(num)
#print(dic)
for key in dic.keys():
    if key==toSearch:
        print(dic[key])
