import shelve

pymodules = dir()
for pymodule in pymodules:
    for inner_func in dir(pymodule):
        print(pymodule, '  :  ', inner_func)

help(shelve)
