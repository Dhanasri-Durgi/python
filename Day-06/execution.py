Python 3.8.2rc1 (tags/v3.8.2rc1:8623e68, Feb 11 2020, 10:46:21) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="python"
>>> t="programming"
>>> s+t #Concatenation
'pythonprogramming'
>>> s*2  #repetition
'pythonpython'
>>> t*5
'programmingprogrammingprogrammingprogrammingprogramming'
>>> '*'*4
'****'
>>> 'd'*6
'dddddd'
>>> 
>>> 
>>> #indexing
>>> s="pyhton flask sql fastapi"
>>> s[3]
't'
>>> s[10]
's'
>>> s[-1]  #negative indexing
'i'
>>> s[-7]
'f'
>>> s[-9]
'l'
>>> 
>>> 
>>> 
>>> #slicing
>>> s[0:5+1:1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[0:5+1:1]
'pyhton'
>>> s[:5+1]
'pyhton'
>>> s[0:]
'pyhton flask sql fastapi'
>>> s{:]
SyntaxError: invalid syntax
>>> s[:]
'pyhton flask sql fastapi'
>>> s{0::2]
SyntaxError: invalid syntax
>>> s[0::2]
'pho ls q atp'
>>> 
>>> 
>>> 
>>> #reversing
>>> s[0:5+1:-1]
''
>>> s[0:6]
'pyhton'
>>> s[0:6:-1]
''
>>> s[::-1]
'ipatsaf lqs ksalf nothyp'
>>> s[-7::-1]
'f lqs ksalf nothyp'
>>> s[-7:]
'fastapi'
>>> s[-11:-9:-1]
''
>>> s[-11:-9]
'sq'
>>> s[-11:-8]
'sql'
>>> s[-9:-12:-1]
'lqs'
>>> 
>>> 
>>> 
>>> #membership
>>> 'python' in s
False
>>> 'pyhton' in s
True
>>> 'sql' not in s
False
>>> 
>>> 
>>> 


>>> 

>>> 
>>> 
>>> #METHODS OF STRING
>>> 
>>> s="python sql java fastapi"
>>> len(s)
23
>>> max(s)
'y'
>>> #gives the character which has max ansci code
>>> min(s)
' '
>>> #here space has the less ansci code value
>>> sorted(s)
[' ', ' ', ' ', 'a', 'a', 'a', 'a', 'f', 'h', 'i', 'j', 'l', 'n', 'o', 'p', 'p', 'q', 's', 's', 't', 't', 'v', 'y']
>>> ord(y)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    ord(y)
NameError: name 'y' is not defined
>>> ord('y')
121
>>> ord(' ')
32
>>> ord(a)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
>>> ord('a')
97
>>> ord('o')
111
>>> ord(0)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    ord(0)
TypeError: ord() expected string of length 1, but int found
>>> ord('0')
48
>>> chr(111)
'o'
>>> chr(2)
'\x02'
>>> chr(87)
'W'
>>> s.upper()
'PYTHON SQL JAVA FASTAPI'
>>> s.lower()
'python sql java fastapi'
>>> t="pyTHon JaVa FASTapi"
>>> t.swapcase()
'PYthON jAvA fastAPI'
>>> s.capitalize()
'Python sql java fastapi'
>>> s.title()
'Python Sql Java Fastapi'
>>> 
>>> 
>>> 
>>> #STRING FORMATTING
>>> s="python"
>>> s.center(30,"*")
'************python************'
>>> s.ljust(40,"*")
'python**********************************'
>>> s.rjust(50,"-")
'--------------------------------------------python'
>>> t=123
>>> t.zfill(5)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    t.zfill(5)
AttributeError: 'int' object has no attribute 'zfill'
>>> '123'.zfill(5)
'00123'
>>> '1'.zfill(6)
'000001'
>>> '1345'.zfill(5)
'01345'
>>> 
>>> 
>>> 
>>> s
'python'
>>> s="python sql java c fastapi"
>>> s.count('a')
4
>>> s.find('z')
-1
>>> s.lfind('a')
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s.lfind('a')
AttributeError: 'str' object has no attribute 'lfind'
>>> s.rfind('a')
22
>>> s.index('a')
12
>>> s.rindex('a')
22
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> 
>>> 
>>> 
>>> 
>>> #Strip()
>>> s='            dhana  sri         '
>>> s
'            dhana  sri         '
>>> s.lstrip()
'dhana  sri         '
>>> s.rstrip()
'            dhana  sri'
>>> s.strip()
'dhana  sri'
>>> 
>>> 
>>> s="python sql java c fastapi"
>>> s
'python sql java c fastapi'
>>> s.replace("a","b")
'python sql jbvb c fbstbpi'
>>> s.replace("p","*")
'*ython sql java c fasta*i'
>>> s.replace("pa","**")
'python sql java c fastapi'
>>> #it will use only when there are continuous set of sequence
>>> s.maketrans("pa","12")
{112: 49, 97: 50}
>>> s.translate(s.maketrans("pa","12"))
'1ython sql j2v2 c f2st21i'
>>> s.translate(s.maketrans('aeiou','*****'))
'pyth*n sql j*v* c f*st*p*'
>>> 