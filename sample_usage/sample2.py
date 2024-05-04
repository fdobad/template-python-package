#!python3

from mypkg import my_module

# v1
print("v1")
retcode = my_module.main(["hola"])
if retcode == 0:
    print("Jalisco won")
elif retcode >= 1:
    print("Jalisco ran into problems, return code is", retcode)

# v2
print("v2")
won = my_module.main(["--retval", "3"])
print("jalisco won with:", won)
