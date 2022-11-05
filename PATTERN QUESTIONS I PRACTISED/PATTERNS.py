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


def square_same_number(n):
    for i in range(n):
        for j in range(n):
            print("4",end=" ")
        print("")



def square_row_wise(n):
    for i in range(1,n+1):
        for j in range(n):
            print(i,end=" ")
        print("")


def star_patterns_reverse(n):
    for i in range(n):
        for j in range(n,i,-1):
            print("*",end=" ")
        print("")


def square_patterns_reverse(n):
    for i in range(n):
        for j in range(n,0,-1):
            print(j,end=" ")
        print("")

def triangular_patterns(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
        print("")

def triangular_pattern_variation(n):
    for i in range(1,n+1):
        for j in range(i):
            z=j+i
            print(z,end=" ")
        print("")

def triangular_pattern_hard_version(n):
    count=0
    for i in range(1,n+1):
        for j in range(i):
            count+=1
            print(count,end=" ")
        print("")

def triangle_normal(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print("")

def rev_triangle_hard(n):
    for i in range(1,n+1):
        for j in range(i):
            z=i-j
            print(z,end=" ")
        print("")

def character_patterns(n):
    for i in range(1,n+1):
        for j in range(n):
            z=ord('A')+j
            z=chr(z)
            print(z,end=" ")
        print("")


def reversed_triangle_patterns(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(n-i,n):
            print("*",end=" ")
        print("")


def isoceles_triangle(n):
    for i in range(1,n+1):
        z=1
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(n-i,n):
            print(z,end=" ")
            z+=1
        z=i-1
        for j in range(n+1,n+i):
            print(z,end=" ")
            z-=1
        print("")

def diamond_pattern(n):
    for i in range(n):
        print(" " * (n-i-1) + "* " * (i+1))
    for i in range(n-1):
        print(" " * (i+1) + "* " * (n-i-1))

def diamond_inverted(n):
    for i in range(n):
        print(" " * (n-i-1) + "*" * (i+1))
    for i in range(n-1):
        print(" "* (i+1) + "*"*(n-i-1))

def pattern_practice(n):
    c=0
    """
    *1*2*3
    *4*5*6
    *7*8*9
    *10*11*12
    """
    for i in range(1,n+1):
        for j in range(((n*(n-1))//2)):
            if j%2==0:
                print("*",end=" ")
            else:
                c+=1
                print(c,end=" ")
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

#square_same_number(n)

"""
OUTPUT:

4 4 4 4 
4 4 4 4 
4 4 4 4 
4 4 4 4 

"""

#square_row_wise(n)

"""
OUTPUT:

1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4

"""


#star_patterns_reverse(n)

"""
OUTPUT:

* * * * 
* * * 
* * 
*

"""

#square_patterns_reverse(n)

"""
OUTPUT:

4 3 2 1 
4 3 2 1 
4 3 2 1 
4 3 2 1 

"""

#triangular_patterns(n)

"""
OUTPUT:

1 
1 2 
1 2 3 
1 2 3 4

"""

#triangular_pattern_variation(n)

"""
OUTPUT:

1 
2 3 
3 4 5 
4 5 6 7

"""

#triangular_pattern_hard_version(n)

"""
OUTPUT:

1 
2 3 
4 5 6 
7 8 9 10

"""

#triangle_normal(n)

"""
OUTPUT:

1 
2 2 
3 3 3 
4 4 4 4

"""

#rev_triangle_hard(n)

"""
OUTPUT:

1 
2 1 
3 2 1 
4 3 2 1

"""

#character_patterns(n)

"""
OUTPUT:

A B C D 
A B C D 
A B C D 
A B C D

"""

#reversed_triangle_patterns(n)

"""
OUTPUT:

      * 
    * * 
  * * * 
* * * *

"""

#isoceles_triangle(n)

"""
OUTPUT:

      1 
    1 2 1 
  1 2 3 2 1 
1 2 3 4 3 2 1

"""
#diamond_pattern(n)

"""

OUTPUT:

   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   *

"""

#diamond_inverted(n)

"""

OUTPUT:

   *
  **
 ***
****
 ***
  **
   *

"""

#pattern_practice(n)

"""
OUTPUT:

*1*2*3
*4*5*6
*7*8*9
*10*11*12

"""