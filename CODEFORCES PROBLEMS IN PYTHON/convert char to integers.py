def replace(s):
    z=""
    #s=Hey
    s=s.lower()
    #s='hey'
    #res={}
    chara=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    res=dict(zip(chara,numbers))
    #RES={CHARACTER:VALUE}
    #RES={A:1,B:2}
    for i in s:
        if i in res:
            z+=str(res[i])
    return z

s="Hey"
print(replace(s))
