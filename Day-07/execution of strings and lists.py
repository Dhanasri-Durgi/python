Python 3.8.2rc1 (tags/v3.8.2rc1:8623e68, Feb 11 2020, 10:46:21) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #STRING TESTING METHODS
>>> 
>>> 
>>> s="Python programming
SyntaxError: EOL while scanning string literal
>>> s="Python programming"
>>> s.istitle()
False
>>> #starting letter of each and every word in a sentence should be capital
>>> s.isstartswith("p")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.isstartswith("p")
AttributeError: 'str' object has no attribute 'isstartswith'
>>> s.startswith("p")
False
>>> s.startswith("P")
True
>>> s.startswith("Pyt")
True
>>> s.startswith("Pytt")
False
>>> s.endswith("ing")
True
>>> 's'.isupper()
False
>>> 'S'.isupper()
True
>>> 'i'.islower()
True
>>> 'code'.isalpha()
True
>>> 'code12'.isalpha()
False
>>> 'code12'.isalnum()
True
>>> 'code@12'.isalnum()
False
>>> 'myvar'.isidentifier()
True
>>> '12myvar'.isidentifier()
False
>>> 'myvar12'.isidentifier()
True
>>> 'myvar@'.isidentifier()
False
>>> 'dhana sri'.isspace()
False
>>> ' dhanasri'.isspace()
False
>>> ' '.isspace()
True
>>> '1234.5'.isdecimal()
False
>>> '12345'.isdecimal()
True
>>> '1234.5'.isdigit()
False
>>> '1234.5'.isnumeric()
False
>>> 
>>> 
>>> s="abcd"
>>> s.split()
['abcd']
>>> s.split('-')
['abcd']
>>> s='abcd'
>>> s.split('-')
['abcd']
>>> 'a b c d'.split()
['a', 'b', 'c', 'd']
>>> 'abcd'.split()
['abcd']
>>> s='a b c d'
>>> s.split("@")
['a b c d']
>>> 'a b c d'.split('@')
['a b c d']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s='hello'
>>> s.encode()
b'hello'
>>> b'hello'.decode()
'hello'
>>> #these encode and decode methods are using to convert the data into bytes  and viceversa
>>> #if we use emojies in the text then it will convert it into the ansci code
>>> 



>>> 

>>> 


>>> 

>>> 
>>> #lists
>>> s=[1,2,3,'a','dhanasri',23.5,23+6j,(1,2,3),{1,2,3}.{1:2,2:3},False,None]
SyntaxError: invalid syntax
>>> s=[1,2,3,'a','dhanasri',23.5,23+6j,(1,2,3),{1,2,3},{1:2,2:3},False,None]
>>> s
[1, 2, 3, 'a', 'dhanasri', 23.5, (23+6j), (1, 2, 3), {1, 2, 3}, {1: 2, 2: 3}, False, None]
>>> #list is heterogeneous
>>> s=[1,1,2,5,6,7]
>>> s
[1, 1, 2, 5, 6, 7]
>>> #it allows duplicates
>>> 
>>> 
>>> 
>>> #operations
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1,2,3,'d']+['h','a','n','a']
[1, 2, 3, 'd', 'h', 'a', 'n', 'a']
>>> [1,2,3]*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> t=['python','sql','fastapi','aws','mysql','html']
>>> t[1]
'sql'
>>> t[3]
'aws'
>>> #indexing
>>> t[::1]
['python', 'sql', 'fastapi', 'aws', 'mysql', 'html']
>>> t[::2]
['python', 'fastapi', 'mysql']
>>> t[::-1]
['html', 'mysql', 'aws', 'fastapi', 'sql', 'python']
>>> t[-3:-1:1]
['aws', 'mysql']
>>> t[-3:0:1]
[]
>>> t[-3::1]
['aws', 'mysql', 'html']
>>> t[-3::-1]
['aws', 'fastapi', 'sql', 'python']
>>> t[4::-1]
['mysql', 'aws', 'fastapi', 'sql', 'python']
>>> t[3:6:-1]
[]
>>> t[-1:-4:-1]
['html', 'mysql', 'aws']
>>> t[-3:-6:-1]
['aws', 'fastapi', 'sql']
>>> #slicing
>>> 
>>> 
>>> 
>>> #methods
>>> len(t)
6
>>> max(t)
'sql'
>>> min(t)
'aws'
>>> sorted(t)
['aws', 'fastapi', 'html', 'mysql', 'python', 'sql']
>>> 
>>> 
>>> 
>>> 
>>> #modify
>>> t.append('c')
>>> t
['python', 'sql', 'fastapi', 'aws', 'mysql', 'html', 'c']
>>> t.extend(['java','css'])
>>> t
['python', 'sql', 'fastapi', 'aws', 'mysql', 'html', 'c', 'java', 'css']
>>> t.insert(3,'c++')
>>> t
['python', 'sql', 'fastapi', 'c++', 'aws', 'mysql', 'html', 'c', 'java', 'css']
>>> t[3]='c'
>>> t
['python', 'sql', 'fastapi', 'c', 'aws', 'mysql', 'html', 'c', 'java', 'css']
>>> t.extend([1,2,3,4])
>>> t
['python', 'sql', 'fastapi', 'c', 'aws', 'mysql', 'html', 'c', 'java', 'css', 1, 2, 3, 4]
>>> t[7]='c++'
>>> t
['python', 'sql', 'fastapi', 'c', 'aws', 'mysql', 'html', 'c++', 'java', 'css', 1, 2, 3, 4]
>>> 