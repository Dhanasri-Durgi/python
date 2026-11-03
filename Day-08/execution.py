Python 3.8.2rc1 (tags/v3.8.2rc1:8623e68, Feb 11 2020, 10:46:21) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[12,34,35,46,56,67]
>>> l
[12, 34, 35, 46, 56, 67]
>>> l.pop()
67
>>> l.pop(1)
34
>>> l.remove(35)
>>> l
[12, 46, 56]
>>> 
>>> del l[2]
>>> l
[12, 46]
>>> l.clear()
>>> l
[]
>>> l.extend([12,23,24,25,56,67,78,79])
>>> l
[12, 23, 24, 25, 56, 67, 78, 79]
>>> l.sorted()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> l
[12, 23, 24, 25, 56, 67, 78, 79]
>>> sorted(l)
[12, 23, 24, 25, 56, 67, 78, 79]
>>> l
[12, 23, 24, 25, 56, 67, 78, 79]
>>> t=[12,56,23,76,34,89,90,987,76]
>>> sorted(t)
[12, 23, 34, 56, 76, 76, 89, 90, 987]
>>> t
[12, 56, 23, 76, 34, 89, 90, 987, 76]
>>> t.sort()
>>> t
[12, 23, 34, 56, 76, 76, 89, 90, 987]
>>> t.reverse()
>>> t
[987, 90, 89, 76, 76, 56, 34, 23, 12]
>>> t.count(76)
2
>>> t.sort(reverse=True)
>>> t
[987, 90, 89, 76, 76, 56, 34, 23, 12]
>>> 
>>> 
>>> n=t
>>> n
[987, 90, 89, 76, 76, 56, 34, 23, 12]
>>> n is t
True
>>> n.append(34)
>>> n
[987, 90, 89, 76, 76, 56, 34, 23, 12, 34]
>>> t
[987, 90, 89, 76, 76, 56, 34, 23, 12, 34]
>>> p.copy(t)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    p.copy(t)
NameError: name 'p' is not defined
>>> p=t.copy()
>>> p
[987, 90, 89, 76, 76, 56, 34, 23, 12, 34]
>>> p.append(45)
>>> p
[987, 90, 89, 76, 76, 56, 34, 23, 12, 34, 45]
>>> t
[987, 90, 89, 76, 76, 56, 34, 23, 12, 34]
>>> id(t)
2177690684096
>>> id(p)
2177690745280
>>> 
>>> 
>>> 
>>> q=[' ',1,2,3,4,5,6]
>>> any(q)
True
>>> all(q)
True
>>> s=[1,2,3,4,5]
>>> any(s)
True
>>> all(s)
True
>>> s.append(" ")
>>> s
[1, 2, 3, 4, 5, ' ']
>>> all(s)
True
>>> k=[0,0.0,[],'',1]
>>> all(K)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    all(K)
NameError: name 'K' is not defined
>>> all(k)
False
>>> s
[1, 2, 3, 4, 5, ' ']
>>> s.pop()
' '
>>> s.append('')
>>> s
[1, 2, 3, 4, 5, '']
>>> all(s)
False
>>> 
>>> 



>>> 
>>> 


>>> 
>>> 


>>> 

>>> 

>>> 

>>> #TUPLE
>>> t=(1,2,3)
>>> t
(1, 2, 3)
>>> t=1,2,3,4,5        #if we dont represent any datatype while declaring then it will consider as a tuple
>>> t
(1, 2, 3, 4, 5)
>>> t=(1)          #if we declare single element like this then it will consider as an integer
>>> t
1
>>> #we should use , after the single element after declaring so that we can represent them as tuple
>>> t=(1,)
>>> t
(1,)
>>> t=(1,2,3.0,4.56,3+5j,'dhanasri',[1,23,4],{1,23,33},{1:2,3:4},False}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> t=(1,2,3.0,4.56,3+5j,'dhanasri',[1,23,4],{1,23,33},{1:2,3:4},False)
>>> t.append(4)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    t.append(4)
AttributeError: 'tuple' object has no attribute 'append'
>>> t[6].append(4)
>>> t
(1, 2, 3.0, 4.56, (3+5j), 'dhanasri', [1, 23, 4, 4], {1, 33, 23}, {1: 2, 3: 4}, False)
>>> len(t)
10
>>> t[7].append("d")
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    t[7].append("d")
AttributeError: 'set' object has no attribute 'append'
>>> t[6].append("d")
>>> t
(1, 2, 3.0, 4.56, (3+5j), 'dhanasri', [1, 23, 4, 4, 'd'], {1, 33, 23}, {1: 2, 3: 4}, False)
>>> (1, 2, 3.0, 4.56, (3+5j), 'dhanasri', [1, 23, 4, 4, 'd'], {1, 33, 23}, {1: 2, 3: 4}, False)
(1, 2, 3.0, 4.56, (3+5j), 'dhanasri', [1, 23, 4, 4, 'd'], {1, 23, 33}, {1: 2, 3: 4}, False)

>>> 
>>> 
>>> (1,2,3,4,5)+(6,7,8,89)
(1, 2, 3, 4, 5, 6, 7, 8, 89)
>>> (1,2,3,4)*5
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> t
(1, 2, 3.0, 4.56, (3+5j), 'dhanasri', [1, 23, 4, 4, 'd'], {1, 33, 23}, {1: 2, 3: 4}, False)
>>> t[-1]
False
>>> t[-3]
{1, 33, 23}
>>> t[:4]
(1, 2, 3.0, 4.56)
>>> t[-4:-1:-1]
()
>>> t[-4:-1]
([1, 23, 4, 4, 'd'], {1, 33, 23}, {1: 2, 3: 4})
>>> t[7:10:-1]
()
>>> t[::-1]
(False, {1: 2, 3: 4}, {1, 33, 23}, [1, 23, 4, 4, 'd'], 'dhanasri', (3+5j), 4.56, 3.0, 2, 1)
>>> 
>>> 
>>> 
>>> t=(12,23,23,65,45,35,76,46,35,87,56,56)
>>> len(t)
12
>>> sorted(t)
[12, 23, 23, 35, 35, 45, 46, 56, 56, 65, 76, 87]
>>> t.sort()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> max(t)
87
>>> min(t)
12
>>> count(56)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    count(56)
NameError: name 'count' is not defined
>>> t.count(56)
2
>>> sum(t)
559
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #SET
>>> s={}
>>> type(s)
<class 'dict'>
>>> #we cannot declare set with {} bcoz it takes it as dict
>>> s=set()  #declaration of set
>>> type(S)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined
>>> type(s)
<class 'set'>
>>> s={1,2,3}
>>> s={1,4,5,6,3,4,7,8,9,0,5,00}
>>> s
{0, 1, 3, 4, 5, 6, 7, 8, 9}
>>> #it is unordered bcoz it is changing the order which we have given
>>> #it also removes duplicate values
>>> 
>>> s={1,2.0,3+4j,'',[1,2,3],{1,2,3},(1,2,3),{1:1,2:2},False}
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    s={1,2.0,3+4j,'',[1,2,3],{1,2,3},(1,2,3),{1:1,2:2},False}
TypeError: unhashable type: 'list'
>>> 
>>> 
>>> 
>>> #here set does not allow mutable datatypes such as list,set,dict
>>> s={1,2.0,3+4j,'',(1,2,3),False}
>>> s
{'', 1, 2.0, False, (1, 2, 3), (3+4j)}
>>> 
>>> 
>>> s={1,2.0,3+4j,'',{1,2,3},(1,2,3),{1:1,2:2},False}
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    s={1,2.0,3+4j,'',{1,2,3},(1,2,3),{1:1,2:2},False}
TypeError: unhashable type: 'set'
>>> s={1,2.0,3+4j,'',(1,2,3),{1:1,2:2},False}
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    s={1,2.0,3+4j,'',(1,2,3),{1:1,2:2},False}
TypeError: unhashable type: 'dict'
>>> s={1,2.0,3+4j,'',(1,2,3),False}
>>> s
{'', 1, 2.0, False, (1, 2, 3), (3+4j)}
>>> 
>>> 
>>> 
>>> a={1,2,3,4,5}
>>> b={1,3,5,7}
>>> a|b
{1, 2, 3, 4, 5, 7}
>>> a&b
{1, 3, 5}
>>> a^b
{2, 4, 7}
>>> a-b
{2, 4}
>>> a.isjoint(b)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    a.isjoint(b)
AttributeError: 'set' object has no attribute 'isjoint'
>>> a.isdisjoint(b)
False
>>> s={8,1,2,34}
>>> t={81,234,12,342}
>>> t.issubset(s)
False
>>> {8,34}.issubset(s)
True
>>> {81,2343}.issubset(t)
False
>>> p={1,3,5,7,9}
>>> p.issuperset({1,3})
True
>>> 