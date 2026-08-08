Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python oprators
'''
1. Arthimetic
'''
'\n1. Arthimetic\n'
a = 10
b = 5
a+b
15
a-b
5
a*b
50
a**b
100000
a/b
2.0
a//b
2
a%2
0
'''
2. comparision operator
'''
'\n2. comparision operator\n'
a>b
True
a<b
False
a>=b
True
a<=b
False
a==b
False
a!=b
True
'''Assignment operators
'''
'Assignment operators\n'
a = a+10
a = 10
a = a+10
a
20
a+=20
a
40
a*=20
a
800
a**2
640000
a**=20
a
11529215046068469760000000000000000000000000000000000000000
a/=10
a
1.1529215046068469e+57
a = 20
a//=2
a
10
a-=1
a
9
'''
4 Relation operators
'''
'\n4 Relation operators\n'
6%2==0 and 3%2==0
False
6%2==0 or 3%2==0
True
's' in 'aeiou'
False
's' not in 'aeiou'
True
6%2 not==0
SyntaxError: invalid syntax
not 3%2==0
True
not6%2==0
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    not6%2==0
NameError: name 'not6' is not defined
not 6%2==0
False
'''
5 Membership operator
'''
'\n5 Membership operator\n'
#string list tuple set dict
s = 'python programming'
'python' in s
True
'java' in s
False
'z' in s
False
'z' not in s
True
l = [1,2,3,4]
3 in l
True
3 not in l
False
t = (1,2,4,5,9)
4 in t
True
4 not in t
False
s = {1,2,3,4,6}
3 in s
True
3 not in s
False
d = {'name':"kartik','batch':65}
     
SyntaxError: unterminated string literal (detected at line 1)
d = {'name':,'karthik','batch':}
     
SyntaxError: expression expected after dictionary key and ':'
d = {'name':,'karthik'}
     
SyntaxError: expression expected after dictionary key and ':'
d = {'name':'karthik','batch'}
     
SyntaxError: ':' expected after dictionary key
'''
identical operator
'''
     
'\nidentical operator\n'
l = [1,2,3,4]
     
m = [1,2,3,4]
     
id(l)
     
2275683950784
id(m)
     
2275682805440
n = m
     
n
     
[1, 2, 3, 4]
>>> id(n)
...      
2275682805440
>>> l is m
...      
False
>>> d = {'name :', "karthik'}
...      
SyntaxError: unterminated string literal (detected at line 1)
>>> d = {'name :', 'karthik'}
...      
>>> name in d
...      
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
>>> 'name' in d
...      
False
>>> 2&2
...      
2
>>> 2|2
...      
2
>>> 2^3
...      
1
>>> 2<<3
...      
16
>>> 12>>2
...      
3
>>> 15<<3
...      
120
>>> 15>>3
...      
1
