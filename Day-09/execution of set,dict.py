Python 3.8.2rc1 (tags/v3.8.2rc1:8623e68, Feb 11 2020, 10:46:21) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={1,2,3,4,56,56,45,34,23,67,67}
>>> s
{1, 2, 3, 4, 34, 67, 45, 23, 56}
>>> sorted(s)
[1, 2, 3, 4, 23, 34, 45, 56, 67]
>>> max(s)
67
>>> min(s)
1
>>> len(s)
9
>>> sum(s)
235
>>> any(s)
True
>>> all(s)
True
>>> s.add('')
>>> s
{'', 1, 2, 3, 4, 34, 67, 45, 23, 56}
>>> all(s)
False
>>> any(s)
True
>>> s.update({23,34,898,900})
>>> s
{'', 1, 2, 3, 4, 34, 67, 900, 898, 45, 23, 56}
>>> s.pop()
''
>>> s.pop()
1
>>> s.pop()
2
>>> s.remove(898)
>>> s.remove(898)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.remove(898)
KeyError: 898
>>> s.discard(898)
>>> s
{3, 4, 34, 67, 900, 45, 23, 56}
>>> s.clear()
>>> s
set()
>>> 
>>> 
>>> s={1,2,3,45,67,54}
>>> a=s
>>> a.add(89)
>>> s
{1, 2, 67, 3, 45, 54, 89}
>>> a
{1, 2, 67, 3, 45, 54, 89}
>>> b=s.copy()
>>> b
{1, 2, 67, 3, 54, 89, 45}
>>> b.add(90)
>>> b
{1, 2, 67, 3, 54, 89, 90, 45}
>>> s
{1, 2, 67, 3, 45, 54, 89}
>>> #this is called shallow copy because the changes in b does not effect original set
>>> 



>>> 
>>> 


>>> 


>>> 
>>> 
>>> #DICT
>>> 
>>> s={}
>>> type(s)
<class 'dict'>
>>> s[1]='int'
>>> s
{1: 'int'}
>>> s[2.0]='float'
>>> s[2+3j]='complex'
>>> s['string']='str'
>>> s[(1,2,3)]='tuple'
>>> s[False]='bool'
>>> s
{1: 'int', 2.0: 'float', (2+3j): 'complex', 'string': 'str', (1, 2, 3): 'tuple', False: 'bool'}
>>> #it allows all immutable datatypes as its keys
>>> 
>>> s[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s[[1,2,3]]='list'
TypeError: unhashable type: 'list'
>>> s[{1,2,3}]='set'
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s[{1,2,3}]='set'
TypeError: unhashable type: 'set'
>>> s[{1:1,2:2}]='dict'
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s[{1:1,2:2}]='dict'
TypeError: unhashable type: 'dict'
>>> 
>>> 
>>> 
>>> #dict does not allow mutable datatypes as its keys
>>> 
>>> s
{1: 'int', 2.0: 'float', (2+3j): 'complex', 'string': 'str', (1, 2, 3): 'tuple', False: 'bool'}
>>> s[1]=1
>>> s
{1: 1, 2.0: 'float', (2+3j): 'complex', 'string': 'str', (1, 2, 3): 'tuple', False: 'bool'}
>>> #dict does not allow duplicate keys it just overwrite the before value of the key with new value
>>> 
>>> 
>>> 
>>> d[1]=1
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    d[1]=1
NameError: name 'd' is not defined
>>> d{}
SyntaxError: invalid syntax
>>> d{}
SyntaxError: invalid syntax
>>> d={}
>>> d[1]=1
>>> d[2]=2.3
>>> d[3]=3+4j
>>> d[4]='dhanasri'
>>> d[5]=[1,2,3]
>>> d[6]=(1,2,3)
>>> d[7]={1,2,3}
>>> d[8]={1:2,2:3}
>>> d[9]=True
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True}
>>> d[10]=1
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1}
>>> #in the respective of values duplicate values are allowes
>>> 
>>> 
>>> 
>>> 
>>> #accessing
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1}
>>> d[2]
2.3
>>> d[8]
{1: 2, 2: 3}
>>> d[11]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    d[11]
KeyError: 11
>>> d.get(11)
>>> d.get(11,'key is not there')
'key is not there'
>>> d.get(6,'key is not there')
(1, 2, 3)
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1}
>>> d[11]=2
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2}
>>> d.update({12:'sri',13:3,14:'j'})
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2, 12: 'sri', 13: 3, 14: 'j'}
>>> 
>>> 
>>> #modification
>>> d[14]
'j'
>>> d[14]='k'
>>> d[14]
'k'
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2, 12: 'sri', 13: 3, 14: 'k'}
>>> d.popitem()
(14, 'k')
>>> d.pop(13)
3
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2, 12: 'sri'}
>>> del d[5]
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2, 12: 'sri'}
>>> d.clear()
>>> d
{}
>>> d={1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2, 12: 'sri', 13: 3, 14: 'j'}
>>> d.keys()
dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
>>> d.values()
dict_values([1, 2.3, (3+4j), 'dhanasri', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 2: 3}, True, 1, 2, 'sri', 3, 'j'])
>>> d.items()
dict_items([(1, 1), (2, 2.3), (3, (3+4j)), (4, 'dhanasri'), (5, [1, 2, 3]), (6, (1, 2, 3)), (7, {1, 2, 3}), (8, {1: 2, 2: 3}), (9, True), (10, 1), (11, 2), (12, 'sri'), (13, 3), (14, 'j')])
>>> d.sorted()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    d.sorted()
AttributeError: 'dict' object has no attribute 'sorted'
>>> sorted(d)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> max(d)
14
>>> min(d)
1
>>> len(d)
14
>>> 
>>> 
>>> 
>>> #setdefault
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2, 12: 'sri', 13: 3, 14: 'j'}
>>> d.setdefault(13)
3
>>> d.setdefault(15)
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2, 12: 'sri', 13: 3, 14: 'j', 15: None}
>>> d.setdefault(16,1)
1
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2, 12: 'sri', 13: 3, 14: 'j', 15: None, 16: 1}
>>> d.setdefault(6,2)
(1, 2, 3)
>>> d
{1: 1, 2: 2.3, 3: (3+4j), 4: 'dhanasri', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 2, 2: 3}, 9: True, 10: 1, 11: 2, 12: 'sri', 13: 3, 14: 'j', 15: None, 16: 1}
>>> 
>>> 
>>> #fromkeys
>>> d=dict.fromkeys({'a','b','c','d'},0)
>>> d
{'b': 0, 'c': 0, 'd': 0, 'a': 0}
>>> 