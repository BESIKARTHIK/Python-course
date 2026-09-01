Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name = input("Enter your name: ")
Enter your name: karthik tarun
>>> name
'karthik tarun'
>>> age = int(input("Enter age: "))
Enter age: 10
>>> age
10
>>> names = input("Enter names: ").split()
Enter names: karthik ayaz
>>> names
['karthik', 'ayaz']
>>> names = input("Enter names: ").split(',')
Enter names: karthik ayaz
>>> names
['karthik ayaz']
>>> names = tuple(input().split())
names
>>> names = tuple(input("Enter names: ").split())
Enter names: karthik ayaz
>>> names
('karthik', 'ayaz')
>>> numbers = list(map(int, input("Enter numbers: ").split()))
... print(numbers)
SyntaxError: multiple statements found while compiling a single statement
>>> numbers = list(map(int, input("Enter numbers: ").split()))
Enter numbers: 10 20 30
>>> numbers
[10, 20, 30]
>>> numbers = tuple(map(int, input("Enter numbers: ").split()))
Enter numbers: 10 20 30
>>> numbers
(10, 20, 30)
>>> numbers = set(map(int, input("Enter numbers: ").split()))
Enter numbers: 10 20 30
>>> numbers
{10, 20, 30}
>>> name,age = input("Enter the name and age: ").split()
Enter the name and age: karthik 20
>>> name
'karthik'
age
'20'
status = eval(input)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    status = eval(input)
TypeError: eval() arg 1 must be a string, bytes or code object
status = eval(input())
True
status
True
type(status)
<class 'bool'>
status = eval(input())
2+3j
status
(2+3j)
typr(status)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    typr(status)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(status)
<class 'complex'>

