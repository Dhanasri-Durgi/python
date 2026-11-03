Python 3.8.2rc1 (tags/v3.8.2rc1:8623e68, Feb 11 2020, 10:46:21) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #arithmetical operators
>>> 
>>> a,b=20,10
>>> a+b
30
>>> a-b
10
>>> a*b
200
>>> a/b
2.0
>>> a//b
2
>>> 9//2
4
>>> 9/2
4.5
>>> a%b
0
>>> 9%2
1
>>> a**b
10240000000000
>>> 2**3
8
>>> 3**3
27
>>> #     + - * / // % **
>>> 
>>> 
>>> #comparision operators
>>> 
>>> a,b = 20,10
>>> a<b
False
>>> a<=b
False
>>> a>b
True
>>> a>=
SyntaxError: invalid syntax
>>> a>=b
True
>>> a==b
False
>>> a!=b
True
>>> 
>>> 
>>> #assignment operators
>>> 
>>> c=10
>>> c+=40
>>> c
50
>>> c-=20
>>> c
30
>>> c*=20
>>> c
600
>>> c/=2
>>> c
300.0
>>> c//=3
>>> c
100.0
>>> c**=10
>>> c
1e+20
>>> c/=10000000
>>> c
10000000000000.0
>>> 
>>> 
>>> 
>>> #logical operators   and or not
>>> 
>>> a=20
>>> b=10
>>> a%2==0 and a>b
True
>>> b%2==0 and b>a
False
>>> b%2==0 or b>a
True
>>> not b>a
True
>>> 
>>> 
>>> 
>>> a%2==0 and a<b or b>a
False
>>> a%2==0 and a<b or a>b
True
>>> 
>>> 
>>> 
>>> #membership operators are used for str,list,tuple,set,dict
>>> 
>>> #membership operators in dict only checks for keys
>>> 
>>> s="dhanasri"
>>> 'd' in s
True
>>> 'y' in s
False
>>> 'h' not in s
False
>>> 
>>> s=[1,2,3,4,'d','h']
>>> 4 in s
True
>>> 5 in s
False
>>> 'd' in s
True
>>> 's' not in s
True
>>> 
>>> s=(1,2,3,4,5,6,'dhanasri')
>>> 'dhanasri' in s
True
>>> 5 in s
True
>>> 
>>> s={1,'a','b','c',2,'r'}
>>> "d" in s
False
>>> "d" not in s
True
>>> "s" not in s
True
>>> 
>>> s={1:'a',2:3,3:4,4:5,5:'dhanasri',6:2,7:'d'}
>>> 'd' in s
False
>>> 7 in s
True
>>> 1 in s
True
>>> 8 in s
False
>>> 
>>> 
>>> #identity operators  is is not
>>> #it checks for the memory references
>>> 
>>> l=[1,2,3,4,5]
>>> m=[1,2,3,4,5]
>>> l==m
True
>>> l is m
False
>>> # l is m means we are referring the memory references for l and m are same
>>> 
>>> id(l)
1980189985600
>>> id(m)
1980189984576
>>> 
>>> n=m  #we are not creating new list but we are just assigning m to n
>>> n is m
True
>>> id (n)
1980189984576
>>> n is not l
True
>>> n
[1, 2, 3, 4, 5]
>>> 