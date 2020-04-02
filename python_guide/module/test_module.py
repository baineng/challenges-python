# -*- coding: utf-8 -*-

print('loading modu1')
import modu1
print(f'modu1 exposed_var is {modu1.exposed_var}')
print(f'modu1 exposed_func is {modu1.exposed_func()}')

modu1.exposed_var = 100

print('loading modu2')
import modu2
print(f'modu2 exposed_var is {modu2.exposed_var}')
print(f'modu2 exposed_func is {modu2.exposed_func()}')
print(f'modu2 exposed_var is {modu2.exposed_var}')

print(f'modu1 exposed_var is {modu1.exposed_var}')
print(f'modu1 exposed_func is {modu1.exposed_func()}')

import submodu1.submodu2.sample
