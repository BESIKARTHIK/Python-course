Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t = ()
t =(1,2,3,4)
t
(1, 2, 3, 4)
t = (2,2,2,2)
t
(2, 2, 2, 2)
t = (1,23.5,'str',[1,2,3],(1,23),{1,2}42:1)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
t = (1,23.5,'str',[1,2,3],(1,23),{1,2},42:1)
SyntaxError: invalid syntax
t = (1,23.5,'str',[1,2,3],(1,23),{1,2})
t
(1, 23.5, 'str', [1, 2, 3], (1, 23), {1, 2})
t = (1,23.5,'str',[1,2,3],(1,23),{1,2},{1:1},True,False)
t
(1, 23.5, 'str', [1, 2, 3], (1, 23), {1, 2}, {1: 1}, True, False)
type(t)
<class 'tuple'>
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,34)*3
(1, 2, 34, 1, 2, 34, 1, 2, 34)
t
(1, 23.5, 'str', [1, 2, 3], (1, 23), {1, 2}, {1: 1}, True, False)
t[1]
23.5
t[-1]
False
t[3:7]
([1, 2, 3], (1, 23), {1, 2}, {1: 1})
t[::-1]
(False, True, {1: 1}, {1, 2}, (1, 23), [1, 2, 3], 'str', 23.5, 1)
t[-1:3:-1]
(False, True, {1: 1}, {1, 2}, (1, 23))
True in t
True
'str' in t
True
'str' not in t
False
t = (13,23,456,54,67,87)
t
(13, 23, 456, 54, 67, 87)
sorted(t)
[13, 23, 54, 67, 87, 456]
max(t)
456
min(t)
13
len(t)
6
t.index(54)
3
t.count(54)
1
all(1,2,3)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    all(1,2,3)
TypeError: all() takes exactly one argument (3 given)
any((1,2,3,00,0))
True
all((1,2,3))
True
t = (1,2,3,4,(1,2,3),6)
t
(1, 2, 3, 4, (1, 2, 3), 6)
t[4].append(5)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t[4].append(5)
AttributeError: 'tuple' object has no attribute 'append'
t[4].append[5]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t[4].append[5]
AttributeError: 'tuple' object has no attribute 'append'
t(4).append(5)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t(4).append(5)
TypeError: 'tuple' object is not callable
t
(1, 2, 3, 4, (1, 2, 3), 6)
t[4].append(5)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    t[4].append(5)
AttributeError: 'tuple' object has no attribute 'append'
t = (1,2,3,4,[1,2,3],6)
t
(1, 2, 3, 4, [1, 2, 3], 6)
t[4].append(5)
t
(1, 2, 3, 4, [1, 2, 3, 5], 6)
s = {}
type(s)
<class 'dict'>
s = set()
s
set()
type(s)
<class 'set'>
s = {1,2,3,4,5,234,56788,2135}
s
{1, 2, 3, 4, 5, 234, 56788, 2135}
s = {1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s.add(65.5)
s.add('str')
s.add({1,2,34})
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s.add({1,2,34})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add((1,2,3))
s
{65.5, 1, (1, 2, 3), 'str'}
s.add({1:2})
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.add({1:2})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(False)
s.add(True)
s
{False, 65.5, 1, (1, 2, 3), 'str'}
1 in s
True
a = {1,2,3,4,5}
b = {3,5,7,8,9}
a|b
{1, 2, 3, 4, 5, 7, 8, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
b-a
{8, 9, 7}
a^b
{1, 2, 4, 7, 8, 9}
a = {1,2,3,4,5}
{1}
{1}
{4,5,6}
{4, 5, 6}
{1},{4,5,6}
({1}, {4, 5, 6})
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}>=a
False
{1,2,3,4}<=a
True
a>={1,2}
True
a>={4,5,6}
False
{1,2,3,4,5}<=a
True
m = {1,2,3}
n = {4,5,6}
n.isdisjoint(m)
True
a.isdisjoint(m)
False
a.isdisjoint(m)
False
a = {1,2,3,4,5}
>>> #[1},{1,2,3},{4,5,6}
>>> a>={1}
True
>>> {1,2,3}<=a
True
>>> {4,5,6}<=a
False
>>> a = {1,2,3,4,49,55,78}
>>> all({1,35,40,2})
True
>>> any({0'1'})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a ={1,2,3,4}
>>> b = {1,2,3,4}
>>> a = {1,2,3,4}
>>> a = b
>>> b
{1, 2, 3, 4}
>>> c= a.copy()
>>> c.add(5)
>>> c
{1, 2, 3, 4, 5}
>>> a
{1, 2, 3, 4}
>>> a.add(5)
>>> a
{1, 2, 3, 4, 5}
>>> a.add(6)
>>> a
{1, 2, 3, 4, 5, 6}
>>> a.update({10,20,30,40})
>>> a
{1, 2, 3, 4, 5, 6, 40, 10, 20, 30}
>>> a.pop()
1
>>> a.pop()
2
>>> a.remove(40)
>>> a
{3, 4, 5, 6, 10, 20, 30}
>>> a.discard(10)
>>> a
{3, 4, 5, 6, 20, 30}
a.clear()
a
set()
