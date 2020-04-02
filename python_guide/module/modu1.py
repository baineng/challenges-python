# -*- coding: utf-8 -*-

import_times = 1
print(f'current import times: {import_times}')

exposed_var = import_times


def exposed_func():
    global exposed_var
    exposed_var += 1
    return exposed_var
