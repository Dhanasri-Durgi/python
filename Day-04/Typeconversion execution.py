Python 3.8.2rc1 (tags/v3.8.2rc1:8623e68, Feb 11 2020, 10:46:21) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #integer conversion
>>> 
>>> a=10
>>> a
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> 
>>> 
>>> #float conversion
>>> 
>>> b=20.2
>>> b
20.2
>>> int(b)
20
>>> complex(b)
(20.2+0j)
>>> str(b)
'20.2'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
>>> bool(b)
True
>>> 
>>> 
>>> #complex conversion
>>> 
>>> c=10+4j
>>> c
(10+4j)
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> str(c)
'(10+4j)'
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
>>> bool(c)
True
>>> 
>>> 
>>> #str conversion
>>> d='10123.4'
>>> d
'10123.4'
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: '10123.4'
>>> float(d)
10123.4
>>> complex(d)
(10123.4+0j)
>>> d='1023'
>>> d
'1023'
>>> int(d)
1023
>>> list(d)
['1', '0', '2', '3']
>>> tuple(d)
('1', '0', '2', '3')
>>> set(d)
{'3', '1', '0', '2'}
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> 
>>> 
>>> 
>>> 
>>> d='dhanasri'
>>> d
'dhanasri'
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'dhanasri'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(d)
ValueError: could not convert string to float: 'dhanasri'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    complex(d)
ValueError: complex() arg is a malformed string
>>> list(d)
['d', 'h', 'a', 'n', 'a', 's', 'r', 'i']
>>> tuple(d)
('d', 'h', 'a', 'n', 'a', 's', 'r', 'i')
>>> set(d)
{'r', 'h', 's', 'i', 'd', 'a', 'n'}
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(d)
True
>>> bool('')
False
>>> 
>>> 
>>> #list conversion
>>> e=[1,2,3,4.5]
>>> e
[1, 2, 3, 4.5]
>>> int(e)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    int(e)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(e)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    float(e)
TypeError: float() argument must be a string or a number, not 'list'
>>> complex(e)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    complex(e)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> str(e)
'[1, 2, 3, 4.5]'
>>> tuple(e)
(1, 2, 3, 4.5)
>>> set(e)
{1, 2, 3, 4.5}
>>> dict(e)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    dict(e)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(e)
True
>>> 
>>> 
>>> #tuple conversion
>>> f=(1,2,3,4,'a')
>>> f
(1, 2, 3, 4, 'a')
>>> int(f)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    int(f)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> float(f)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    float(f)
TypeError: float() argument must be a string or a number, not 'tuple'
>>> complex(f)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    complex(f)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> str(f)
"(1, 2, 3, 4, 'a')"
>>> list(f)
[1, 2, 3, 4, 'a']
>>> set(f)
{1, 2, 3, 4, 'a'}
>>> dict(f)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    dict(f)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(f)
True
>>> 
>>> 
>>> #set conversion
>>> g={1,2,3,4,'dhanasri",'f'}
   
SyntaxError: EOL while scanning string literal
>>> g={1,2,3,4,"dhanasri",'f'}
>>> g
{1, 2, 3, 4, 'dhanasri', 'f'}
>>> int(g)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    int(g)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> float(g)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    float(g)
TypeError: float() argument must be a string or a number, not 'set'
>>> complex(g)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    complex(g)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> str(g)
"{1, 2, 3, 4, 'dhanasri', 'f'}"
>>> list(g)
[1, 2, 3, 4, 'dhanasri', 'f']
>>> tuple(g)
(1, 2, 3, 4, 'dhanasri', 'f')
>>> dict(g)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    dict(g)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(g)
True
>>> 
>>> 
>>> #dict conversion
>>> h={1:2,2:3,3:4,4:'dhanasri',5:1000}
>>> h
{1: 2, 2: 3, 3: 4, 4: 'dhanasri', 5: 1000}
>>> int(h)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    int(h)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
>>> float(h)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    float(h)
TypeError: float() argument must be a string or a number, not 'dict'
>>> complex(h)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    complex(h)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(h)
"{1: 2, 2: 3, 3: 4, 4: 'dhanasri', 5: 1000}"
>>> list(h)
[1, 2, 3, 4, 5]
>>> tuple(h)
(1, 2, 3, 4, 5)
>>> set(h)
{1, 2, 3, 4, 5}
>>> bool(h)
True
>>> 
>>> 
>>> #bool conversion
>>> i=true
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    i=true
NameError: name 'true' is not defined
>>> i=True
>>> j=False
>>> i
True
>>> j
False
>>> int(i)
1
>>> int(j)
0
>>> float(i)
1.0
>>> float(j)
0.0
>>> complex(i)
(1+0j)
>>> complex(j)
0j
>>> str(i)
'True'
>>> str(j)
'False'
>>> list(i)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    list(i)
TypeError: 'bool' object is not iterable
>>> list(j)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    list(j)
TypeError: 'bool' object is not iterable
>>> tuple(i)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    tuple(i)
TypeError: 'bool' object is not iterable
>>> tuple(j)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    tuple(j)
TypeError: 'bool' object is not iterable
>>> set(i)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    set(i)
TypeError: 'bool' object is not iterable
>>> set(j)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    set(j)
TypeError: 'bool' object is not iterable
>>> dict(i)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    dict(i)
TypeError: 'bool' object is not iterable
>>> dict(j)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    dict(j)
TypeError: 'bool' object is not iterable
>>> 