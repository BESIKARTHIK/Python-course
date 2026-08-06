Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
b = 10.5
type(b)
<class 'float'>
c = 10 + 5j
typr(c)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    typr(c)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(c)
<class 'complex'>
s = "codegnan"
type(s)
<class 'str'>
id(s)
1566205924080
s += "python"
print(s)
codegnanpython
id(s)
1566205923888
l = {1,2,3,4,4,6,5}
type(l)
<class 'set'>
l = [1,2,3,4,5,4]
>>> type(l)
<class 'list'>
>>> t = (1,2,3,5,4,6)
>>> type(t)
<class 'tuple'>
>>> l.append[12]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l.append[12]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l = [1,2,3,4,5]
>>> type(l)
<class 'list'>
>>> l.append(12)
>>> print(l)
[1, 2, 3, 4, 5, 12]
>>> s = [1,2,"Karthik"]
>>> typr(s)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    typr(s)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> s = {1,2,"Karthik"}
>>> type(s)
<class 'set'>
>>> D = {student : "Karthik", age : 21}
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    D = {student : "Karthik", age : 21}
NameError: name 'student' is not defined
>>> D = {'student': 'karthik','age':21}
>>> type(D)
<class 'dict'>
>>> a = True
>>> b = False
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
