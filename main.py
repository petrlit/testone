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
