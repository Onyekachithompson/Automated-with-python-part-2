Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = True
spam
True
42 == 42
True
42 == 99
False
2 != 3
True
2 != 2
False
#As you might expect, == (equal to) evaluates to True when the values 
on both sides are the same, and != (not equal to) evaluates to True when 
the two values are different. The == and != operators can actually work with 
values of any data type.
SyntaxError: invalid syntax
'hello' == 'hello'
True
'hello' == 'Hello'
False
'dog' != 'cat'
True
True == True
True
True != False
True
42 == 42.0
True
42 == '42'
False
#Note that an integer or floating-point value will always be unequal to a 
string value. The expression 42 == '42' evaluates to False because Python 
considers the integer 42 to be different from the string '42'.
The <, >, <=, and >= operators, on the other hand, work properly only 
with integer and floating-point values.
SyntaxError: invalid syntax
42 < 100
True
42 > 100
False
42 < 42
False
42 == 42
True
eggcount = 42
eggcount <= 42
True
myAge = 29
myAge >= 10
True
>>> True and True
True
>>> True and False
False
>>> False or True
True
>>> False or False
False
>>> not True
False
>>> not not not not not True
False
>>> not not True
True
>>> not not not True
False
>>> not not not not True
True
>>> #Much like using double negatives in speech and writing, you can nest 
not operators , though there’s never not no reason to do this in real programs.
SyntaxError: invalid character '’' (U+2019)
(4 < 5) and (5 < 6)
True
(4 < 5) and (9 < 6)
False
(3 < 6) and (4 > 9)
False
(1 == 2) and (2 == 2)
False
(1 == 2) or (2 == 2)
True
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True
if name == 'Mary':
    print('Hello Mary')

    
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    if name == 'Mary':
NameError: name 'name' is not defined
