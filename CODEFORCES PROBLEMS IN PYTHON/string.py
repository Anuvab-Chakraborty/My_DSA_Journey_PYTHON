s="here in this sentence , test is present"
#s="here in this sentence ,is not present"
z="test"
if s.find(z)==-1:print("Not here")
else:
    res=s.split(z,1)
    print(res[1])
