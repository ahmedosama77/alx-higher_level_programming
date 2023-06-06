#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{}Is positive".format(number))
elif number == 0:
    print("{}Is zero".format(number))
else:
    print("{}Is negative".format(number))
