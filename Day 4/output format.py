Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = 10
>>> b = 10.5
>>> c ='codegnan'
>>> print(a,b,c)
10 10.5 codegnan
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 10.5 c= codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=10b=10.5c=codegnan
>>> print("a=",a,"b=",b,"c=",c, sep='\n')
a=
10
b=
10.5
c=
codegnan
>>> print("a=",a,"b=",b,"c=",c, sep='\t')
a=	10	b=	10.5	c=	codegnan
>>> print("a=",a,"b=",b,"c=",c, sep='\t', end='\n')
a=	10	b=	10.5	c=	codegnan
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.5 c=codegnan
