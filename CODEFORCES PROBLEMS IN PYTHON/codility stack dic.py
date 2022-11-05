#from collections import OrderedDict
l=[]
s=""
l1=[10,20,30]
l2=[8,19]
l3=[1,7]
l1.sort(reverse=True)
l2.sort(reverse=True)
l3.sort(reverse=True)
#print(l1)
#print(l2)
#print(l3)
l1_val=[1 for i in range (len(l1))]
l2_val=[2 for i in range(len(l2))]
l3_val=[3 for i in range(len(l3))]
#print(l1_val)
dict1=dict(zip(l1,l1_val))
#print(dict1)
dict2=dict(zip(l2,l2_val))
dict3=dict(zip(l3,l3_val))
dict1.update(dict2)
dict1.update(dict3)
#print(dict1)
final_dict=(sorted(dict1.items(),reverse=True))
#print(final_dict)
for key,value in final_dict:
    l.append(str(value))
#print(l)
s="".join(l)
print(""+s)
