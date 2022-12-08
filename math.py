from decimal import Decimal

x = input("insert x: ")
y = input("insert y: ")
z = float(x) * float(y)
print(z == 0.3)
print(z)  #float value
print(type(z))
print(round(z))  #round to whole number
print(round(z, 8))  #round to 8 numbers after . zeros deleted
print("%.8f" % z)  #round to 8 numbers afetr . zeroes not deleted

z = round(z, 4)
print(z, z == 0.3, type(z))

w = Decimal(x) * Decimal(y)
print(w) #decimal
print(w == Decimal('0.3'))
print(type(w))
print('----------------------------------------')



"""if x.isdigit():
    check_int = isinstance(x, int)
    check_float = isinstance(x, float)
    if check_int:
        print(x * 3)
    elif check_float:
        print(x * 1)
else:
    print("non digit symbols")"""
