import os

try:
    hostname = '172.31.38.130'
    #ping = 4
    #response = os.system(f'ping {hostname} -c{ping}')
    response = os.system(f'ping {hostname}')
    os.name
except Exception as ex:
    print(ex)
