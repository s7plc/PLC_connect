from time import sleep, time
from pycomm3 import LogixDriver
from ping import response

print(response)

print('------------------Connect to PLC------------------------------')
start_time = time()
with LogixDriver('192.168.32.39/1', init_tags=True) as plc:
    # g = plc.get_plc_name()
    # k = plc.read('_010R01:I.Data[0]')
    stop_time = time()
    print(f"Read tags time = {stop_time - start_time} sec")
    for i in range(1, 11):
        start_time1 = time()
        k = plc.read('HMI_IND')
        finish_time = time() - start_time1
        print('------------------------------------------------')
        print(f"try # {i}")
        print(f"value of {k[0]} is {k[1]}")
        print(f"tag read for = {finish_time * 100} ms")
        i += i
        sleep(1)
