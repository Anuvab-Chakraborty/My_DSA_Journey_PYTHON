# pattern problems
def normal_tri(n):
    for i in range(n+1):
        for j in range(i+1):
            print(j,end=" ")
        print(" ")

def normal_star(n):
    for i in range(n+1):
        for j in range(i+1):
            print("*",end=" ")
        print("")

def square_stars(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print("")


def square_number(n):
    for i in range(n):
        for j in range(1,n+1):
            print(j,end=" ")
        print("")

n=4
#normal_tri(n)
"""OUTPUT:
0  
0 1  
0 1 2  
0 1 2 3  
0 1 2 3 4  

"""
#normal_star(n)
"""
OUTPUT:
* 
* * 
* * * 
* * * * 
* * * * * 

"""
#square_stars(n)

"""
OUTPUT:
* * * * 
* * * * 
* * * * 
* * * * 
"""

#square_number(n)

"""
OUTPUT:

1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 

"""

