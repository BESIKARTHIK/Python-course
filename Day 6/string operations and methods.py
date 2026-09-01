Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 'python'
b = 'programming'
a+b
'pythonprogramming'
fname = 'karthik'
lname = 'besi'
fname + lname
'karthikbesi'
s = "codegnan"
s*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
'karthik'*5
'karthikkarthikkarthikkarthikkarthik'
s = "codegnan"
s[1]
'o'
s[-1]
'n'
names = 'karthik , tarun'
names
'karthik , tarun'
names[:8]
'karthik '
names[9:14]
' taru'
>>> names[9:15]
' tarun'
>>> names[-9:]
'k , tarun'
>>> names[-8]
' '
>>> names[-10:]
'ik , tarun'
>>> names[-11:]
'hik , tarun'
>>> 'hik , tarun'
'hik , tarun'
>>> names[-6:]
' tarun'
>>> names[-1:-6:-1]
'nurat'
>>> k in names
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    k in names
NameError: name 'k' is not defined
>>> 'k' in names
True
>>> 'k' not in names
False
>>> 't' in names
True
>>> len(names)
15
>>> crd('k')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    crd('k')
NameError: name 'crd' is not defined. Did you mean: 'ord'?
>>> ord('a')
97
>>> ord('u')
117
>>> chr(12)
'\x0c'
>>> chr(100)
'd'
chr(40)
'('
chr(117)
'u'
sorted(names)
[' ', ' ', ',', 'a', 'a', 'h', 'i', 'k', 'k', 'n', 'r', 'r', 't', 't', 'u']
max(names)
'u'
min(names)
' '
s = 'karthik'
s.upper()
'KARTHIK'
s.lower()
'karthik'
s.swapcase()
'KARTHIK'
s.captalize()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
s.capitalize()
'Karthik'
s.title()
'Karthik'
'STRWEENnmwskerr'.casefold()
'strweennmwskerr'
s.centre(20,'*')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.centre(20,'*')
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
s.center(20,'*')
'******karthik*******'
s.ljust(10,'*')
'karthik***'
s.rjust(10,'*')
'***karthik'
'123'zfill(4)
SyntaxError: invalid syntax
'123'.zfill(4)
'0123'
'65'.zfill(5)
'00065'
s
'karthik'
s.find('k')
0
s.find('a')
1
s.rfind('k')
6
s.index('k')
0
s.rindex('k')
6
s.count('k')
2
s.count('a')
1
s.replace('k','1')
'1arthi1'
s.replace('karthik','Tarun')
'Tarun'
s.maketrans('aeiou','&%$^#')
{97: 38, 101: 37, 105: 36, 111: 94, 117: 35}
s.translate(s.maketrans('aeiou','&%$^#'))
'k&rth$k'
