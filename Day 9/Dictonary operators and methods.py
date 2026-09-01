Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d = {}
type(d)
<class 'dict'>
d = {1:4,2:3,4:5}
d
{1: 4, 2: 3, 4: 5}
d = {}
d
{}
d[1]=1
d[12.3]=1
d['str']=1
d[(1,2,3)]=1
d[(2+5j)]=1
d[{1,2,3}]=1
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d[{1,2,3}]=1
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{1,2,3}]=1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d[{1,2,3}]=1
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[False] = 1
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+5j): 1, False: 1}
d[1]=1
d[2]=12.5
d[3]='str'
d[4]=[1,2,3]
d[5]={1,2,3}
d[6]=(1,2,3)
d[7]=12+5j
d[8]=True
d[9]=frozenset({1,2,3})
d[10]={1:1,2:3}
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+5j): 1, False: 1, 2: 12.5, 3: 'str', 4: [1, 2, 3], 5: {1, 2, 3}, 6: (1, 2, 3), 7: (12+5j), 8: True, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 3}}
data = {'name':'karthik','course':'CSE'}
data
{'name': 'karthik', 'course': 'CSE'}
data['name']
'karthik'
data.get('age','key is not in the data')
'key is not in the data'
'course'in data
True
data.get('name','key is not present')
'karthik'
data['age']=21
data
{'name': 'karthik', 'course': 'CSE', 'age': 21}
data.update({'phnno':98765321,'email':'karthik@gmail.com'})
data
{'name': 'karthik', 'course': 'CSE', 'age': 21, 'phnno': 98765321, 'email': 'karthik@gmail.com'}
id(data)
1794953329472
data.pop()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
data.pop('email')
'karthik@gmail.com'
data
{'name': 'karthik', 'course': 'CSE', 'age': 21, 'phnno': 98765321}
data.popitem()
('phnno', 98765321)
del 'course' in data
SyntaxError: cannot delete comparison
del data['course']
data
{'name': 'karthik', 'age': 21}
data.clear()
data
{}
data={'name': 'karthik', 'course': 'CSE', 'age': 21, 'phnno': 98765321, 'email': 'karthik@gmail.com'}
data
{'name': 'karthik', 'course': 'CSE', 'age': 21, 'phnno': 98765321, 'email': 'karthik@gmail.com'}
data.keys()
dict_keys(['name', 'course', 'age', 'phnno', 'email'])
data.values()
dict_values(['karthik', 'CSE', 21, 98765321, 'karthik@gmail.com'])
data.items()
dict_items([('name', 'karthik'), ('course', 'CSE'), ('age', 21), ('phnno', 98765321), ('email', 'karthik@gmail.com')])
max(data)
'phnno'
min(data)
'age'
d = {1:1,2:2}
m = d
m = {3:3}
m
{3: 3}
m =d
m
{1: 1, 2: 2}
d
{1: 1, 2: 2}
m = 3:3
SyntaxError: invalid syntax
m[3]=3
m
{1: 1, 2: 2, 3: 3}
d
{1: 1, 2: 2, 3: 3}
n = d.copy()
>>> n
{1: 1, 2: 2, 3: 3}
>>> n[4]=4
>>> n
{1: 1, 2: 2, 3: 3, 4: 4}
>>> d
{1: 1, 2: 2, 3: 3}
>>> data
{'name': 'karthik', 'course': 'CSE', 'age': 21, 'phnno': 98765321, 'email': 'karthik@gmail.com'}
>>> data.get('py')
>>> data.setdefault('py',2026)
2026
>>> data.setdefault('name',tarun)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    data.setdefault('name',tarun)
NameError: name 'tarun' is not defined
>>> data.setdefault('name','tarun')
'karthik'
>>> data
{'name': 'karthik', 'course': 'CSE', 'age': 21, 'phnno': 98765321, 'email': 'karthik@gmail.com', 'py': 2026}
>>> data.setdefault('key',2026)
2026
>>> data
{'name': 'karthik', 'course': 'CSE', 'age': 21, 'phnno': 98765321, 'email': 'karthik@gmail.com', 'py': 2026, 'key': 2026}
>>> data.setdefault('age',2026)
21
>>> data
{'name': 'karthik', 'course': 'CSE', 'age': 21, 'phnno': 98765321, 'email': 'karthik@gmail.com', 'py': 2026, 'key': 2026}
>>> dict fromkeys([['python','mysql','java': 0])
...               
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> dict fromkeys(['python','mysql','java': 0])
...               
SyntaxError: invalid syntax
>>> dict.fromkeys(['python','mysql','java'],0)
...               
{'python': 0, 'mysql': 0, 'java': 0}
>>> data
...               
{'name': 'karthik', 'course': 'CSE', 'age': 21, 'phnno': 98765321, 'email': 'karthik@gmail.com', 'py': 2026, 'key': 2026}
