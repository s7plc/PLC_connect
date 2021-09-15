#!/usr/bin/env python3

x = input("insert integer: \n")
y = x == "1"
print(y)

try:
    x = float(x)
    if x != 0:
        x = 5 / x
        print(x)
    else:
        print("you tried divide by 0")
except ValueError:
    print('it is not digit')
