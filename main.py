#!/usr/bin/env python3

print('Привіт, Світ!')

x = 100/3
form = '{0:.3}'.format(x)
print(form)

name = '_TRAMP_'
fname = '{0:$^22}'.format(name)
print(fname)
