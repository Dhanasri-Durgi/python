Python 3.8.2rc1 (tags/v3.8.2rc1:8623e68, Feb 11 2020, 10:46:21) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Bitwise operators
>>> '''
& is represented as bitwise and
| is representd as bitwise or
^ is represented as bitwise exclusive or
<< is represented as leftshift
>> is representde as rightshift'''
'\n& is represented as bitwise and\n| is representd as bitwise or\n^ is represented as bitwise exclusive or\n<< is represented as leftshift\n>> is representde as rightshift'
>>> 
>>> 5&14
4
>>> '''
0101 & 1110 = 0100 it is 4
'''
'\n0101 & 1110 = 0100 it is 4\n'
>>> 5|14
15
>>> '''
0101 | 1110 = 1111 it is  15
'''
'\n0101 | 1110 = 1111 it is  15\n'
>>> 5^14
11
>>> '''
0101 ^ 1110 = 1011 it is 11'''
'\n0101 ^ 1110 = 1011 it is 11'
>>> 
>>> ~11
-12
>>> ~90
-91
>>> ~3
-4
>>> 2<<2
8
>>> 2<<3
16
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #How to take input from the user
>>> 
>>> a=input("enter the string:")
enter the string:234
>>> a
'234'
>>> #here we have given int as inp but it is showing the input as str because the default type of inp fun is string
>>> 
>>> a=int(input("enter the string:"))
enter the string:234
>>> type(a)
<class 'int'>
>>> 
>>> a=float(input("enter the float:"))
enter the float:234
>>> a
234.0
>>> type(a)
<class 'float'>
>>> 
>>> 
>>> 
>>> 
>>> #take list of elements from the user
>>> 
>>> a=list(input())
1,2,3,4,5,6
>>> a
['1', ',', '2', ',', '3', ',', '4', ',', '5', ',', '6']
>>> a=list(input())
12,23,34,567,6543
>>> a
['1', '2', ',', '2', '3', ',', '3', '4', ',', '5', '6', '7', ',', '6', '5', '4', '3']
>>> #here it is taking each and every digit as one character so we need to use split() to take list values
>>> 
>>> a=list(input().split())
122,23,34,45
>>> a
['122,23,34,45']
>>> a=input().split()
12,23,45,667
>>> a
['12,23,45,667']
>>> a=input().split(',')
12,34,45
>>> a
['12', '34', '45']
>>> #here it is taking integers as str .....to represent them into int we nned to use map() which is a lazy loader which iterates each and every element into int
>>> a=map(int,input().split(' '))
12 23 45 65
>>> a
<map object at 0x000002373A81B100>
>>> a=list(map(int,input().split(' ')))
12 23 45 65 456
>>> a
[12, 23, 45, 65, 456]
>>> #here map() gives the object's  memory reference so we need to use list() to get output
>>> #map(type of element that we need to convert,input).........representation of map function
>>> 
>>> 
>>> 
>>> 
>>> a=tuple(map(int,input().split()))
12 23 45 65
>>> a
(12, 23, 45, 65)
>>> a=tuple(map(float,input().split()))

>>> 12 23 45 65
SyntaxError: invalid syntax
>>>  a=tuple(map(float,input().split()))
 
SyntaxError: unexpected indent
>>> a=tuple(map(float,input().split()))
12 23 34 45 67
>>> a
(12.0, 23.0, 34.0, 45.0, 67.0)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #how to take multiple inputs from the user
>>> 
>>> a,b,c = input().split()
12 23 34
>>> a
'12'
>>> b
'23'
>>> c
'34'
>>> a,b,c = list(map(int,input().split()))
12 23 34
>>> a
12
>>> b
23
>>> c
34
>>> email,password = tuple(input().split())
dhanasri@gmail.com 12345
>>> email
'dhanasri@gmail.com'
>>> password
'12345'
>>> #we can use any datatype such as list,tuple,set
>>> 
>>> a,b = set(map(float,input().split()))
12.3 45.6
>>> a
12.3
>>> b
45.6
>>> 
>>> 
>>> 
>>> #eval() is used when the user specically wants to mention the datatype he is using
>>> a=eval(input())
"dhanasri"
>>> a
'dhanasri'
>>> a=eval(input())
12
>>> a
12
>>> a=eval(input())
12.88
>>> a
12.88
>>> a=eval(input())
2+3j
>>> a
(2+3j)
>>> a=eval(input())
[1,2,34,45]
>>> a
[1, 2, 34, 45]
>>> a=eval(input())
('d','h','a','n','a','s','r','i')
>>> a
('d', 'h', 'a', 'n', 'a', 's', 'r', 'i')
>>> a=eval(input())
{1,2,3,4,5}
>>> a
{1, 2, 3, 4, 5}
>>> a=eval(input())
{1:1,2:'d',3:'h',4:5}
>>> a
{1: 1, 2: 'd', 3: 'h', 4: 5}
>>> a=eval(input())
True
>>> type(a)
<class 'bool'>
>>> a=eval(input.split())
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a=eval(input.split())
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> a=eval(input().split())
12 34 45 56
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a=eval(input().split())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> a=eval(input().split())
[1,2,3,4,5]
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    a=eval(input().split())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #OUTPUT FORMATTING
>>> 
>>> a,b,c=10,20.22,"codegnan"
>>> print(a,b,c)
10 20.22 codegnan
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 20.22 c= codegnan
>>> print("a=",a,"b=",b,"c=",c,sep="")
a=10b=20.22c=codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='-')
a=-10-b=-20.22-c=-codegnan
>>> print("a=",a,"b=",b,"c=",c,end='\n\n')
a= 10 b= 20.22 c= codegnan

>>> print("a=",a,"b=",b,"c=",c,end='@')
a= 10 b= 20.22 c= codegnan@
>>> 
>>> 
>>> #imp form
>>> print(f'a={a},b={b},c={c}')
a=10,b=20.22,c=codegnan
>>> print(f'a={a} b={b} c={c}')
a=10 b=20.22 c=codegnan
>>> 
>>> 
>>> print('a=%d b=%f c=%s')
a=%d b=%f c=%s
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=20.220000 c=codegnan
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=20.22 c=codegnan
>>> 
>>> 
>>> #using format method
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=20.22 c=codegnan
>>> print('a={} b={} c={}'.format(b,c,a))
a=20.22 b=codegnan c=10
>>> 