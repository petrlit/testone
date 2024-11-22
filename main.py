#!/usr/bin/env python3

print('Hello, World!')

x = 100/3
form = '{0:.3}'.format(x)
print(form)

name = '_TRAMP_'
fname = '{0:$^22}'.format(name)
print(fname)

name1 = 'Вася'
action = 'читает'
object = 'книгу'
print('{0} {1} {2}'.format(name1, action, object))
_23_name = 43
print(_23_name)
кілька = 67
print(кілька)

s = '''Это строка.
Это вторая строка'''
print(s)

s = 'Это строка. \
Это  строка продолжается'
print(s)