from time import asctime, sleep
from pycomm3 import LogixDriver


print('------------------Connect to PLC------------------------------')
try:
    with LogixDriver('10.228.4.4/3', init_tags=True) as plc:
        x = plc.write('Probe', False)
        print(plc.read('Probe'))
        sleep(1)
        x = plc.write('Probe', 1)
        sleep(1)
        status = plc.read('Probe')

except Exception as ex:
    print(f"Failed at {asctime()} with error: {ex}")
