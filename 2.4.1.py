Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= 10
>>> b=10.1
>>> c= 10+ 2j
>>> d= True
>>> e= 'good'
>>> print(type())
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(type())
TypeError: type() takes 1 or 3 arguments
>>> print(type(a))
<class 'int'>
>>> print(type(b))
<class 'float'>
>>> print(type(c))
<class 'complex'>
>>> print(type(d))
<class 'bool'>
>>> print(type(e))
<class 'str'>
>>> A=486
>>> B=0b110
>>> C=0o56
>>> D=0xAC
>>> E=3.14
>>> F=4-4j
>>> print(type(A))
<class 'int'>
>>> print(type(B))
<class 'int'>
>>> print(type(C))
<class 'int'>
>>> print(type(D))
<class 'int'>
>>> print(type(E))
<class 'float'>
>>> print(type(F))
<class 'complex'>
