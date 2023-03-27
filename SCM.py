from time import asctime
from pycomm3 import LogixDriver

x = {
    "19": 19,
    "21": 21,
    "22": 22,
    "24": 24,
    "25": 25,
    "27": 27,
    "32": 32,
    "35": 35,
    "38": 38,
    "42": 42,
    "44": 44,
    "50": 50,
    "54": 54,
    "55": 55,
    "57": 57,
    "63": 63,
    "67": 67,
    "70": 70,
    "79": 79,
    "81": 81,
    "83": 83,
    "86": 86,
    "87": 87,
    "94": 94,
    "96": 96,
    "129": 129,
    "148": 148}
print('------------------Connect to PLC------------------------------')
try:
    with LogixDriver('10.228.4.4/3', init_tags=True) as plc:
        for i in x:
            x[i] = plc.read(f'Drops.connection_fault_{i}')
            print(x[i][0], "=", x[i][1])
except Exception as ex:
    print(f"Failed at {asctime()} with error: {ex}")
