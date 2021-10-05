from time import sleep, time, asctime
from pycomm3 import LogixDriver
from ping import response
print(response)

print('------------------Connect to PLC------------------------------')
start_time = time()
try:
    with LogixDriver('192.168.32.39/1', init_tags=True) as plc:
        stop_time = time()
        print(f"Read tags time = {stop_time - start_time} sec")
        # print(plc.get_plc_time())
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
except Exception as ex:
    print(f"Failed at {asctime()} with error: {ex}")
