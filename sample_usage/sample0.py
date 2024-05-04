#!python3

from mypkg.my_module import jalisco_nunca_pierde

challenge = 3
print("Challenging Jalisco with:", challenge)
retval = jalisco_nunca_pierde(challenge)
print("Jalisco answer:", retval)
if retval > challenge:
    print("Jalisco wins!")
