from time import asctime
from pycomm3 import LogixDriver

print('------------------Connect to PLC------------------------------')
value = 0
try:
    with LogixDriver('172.31.38.130/0', init_tags=True) as plc:
        cell1 = plc.read('Cell1_Scanners_OK')
        cell2 = plc.read('Cell2_Scanners_OK')
        scanner5 = plc.read('Local:5:I.Pt00.Data')
        scanner3 = plc.read('Local:5:I.Pt03.Data')
        scanner8 = plc.read('Local:5:I.Pt02.Data')
        #for value in range(100):
        #    plc.write('test_dint', value)
        #    test = plc.read('test_dint')
        #   print(test)
        #plc.write('test_real', value)
        #test = plc.read('test_real')

    print(f"value of {cell1[0]} is {cell1[1]}")
    print(f"value of Scanner 5 is {scanner5[1]}")
    print(f"    value of Scanner 3 is {scanner3[1]}")
    print(f"    value of Scanner 8 is {scanner8[1]}")
    print(f"value of {cell2[0]} is {cell2[1]}")
    print("test")
except Exception as ex:
    print(f"Failed at {asctime()} with error: {ex}")
