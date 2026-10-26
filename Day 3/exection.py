Python 3.8.2rc1 (tags/v3.8.2rc1:8623e68, Feb 11 2020, 10:46:21) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> b=12.3
>>> type(b)
<class 'float'>
>>> c=3+5j
>>> c
(3+5j)
>>> type(c)
<class 'complex'>
>>> 
>>> #strings
>>> s="codegnan"
>>> s
'codegnan'
>>> type(s)
<class 'str'>
>>> id(s)  #memory referance
2675176413744
>>> s+="institute"
>>> s
'codegnaninstitute'
>>> id(s)
2675176410368
>>> 
>>> 
>>> #list
>>> k=[1,2,3.4,6,'a']
>>> type(k)
<class 'list'>
>>> id(k)
2675176820800
>>> k.append("dhanasri")
>>> k
[1, 2, 3.4, 6, 'a', 'dhanasri']
>>> id(k)
2675176820800
>>> k.pop(2)
3.4
>>> id(k)
2675176820800
>>> p=[1,1,1,1,1]
>>> 
>>> 
>>> #tuple
>>> t=(1,2,3.4,'a','b')
>>> type(t)
<class 'tuple'>
>>> id(t)
2675176431504
>>> t.pop()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> 
>>> 
>>> 
>>> #set
>>> s={12341,23,45,45,32,43,34,34,56}
>>> s
{32, 34, 43, 45, 12341, 23, 56}
>>> type(s)
<class 'set'>
>>> 
>>> 
>>> #dict
>>> d={1:"one",2:4,3:[1,2,3],4:(1,2,3)}
>>> d
{1: 'one', 2: 4, 3: [1, 2, 3], 4: (1, 2, 3)}
>>> pro={"pro_name":"laptop","price":55000,"discount":10}
>>> pro
{'pro_name': 'laptop', 'price': 55000, 'discount': 10}
>>> 
>>> 
>>> #bool
>>> s=True
>>> y=False
>>> s
True
>>> type(y)
<class 'bool'>
>>> 
>>> 
>>> #None
>>> s=None
>>> type(s)
<class 'NoneType'>
>>> 