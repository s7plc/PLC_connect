from pycomm3 import LogixDriver


def read_udt():
    with LogixDriver('192.168.32.39/1') as plc:
        # return plc.read('HMI_IND')
        return plc.get_tag_list(program='*')

print(read_udt())



