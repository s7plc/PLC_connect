from pycomm3 import LogixDriver


def read_udt(tag):
    with LogixDriver('192.168.32.39/1') as plc:
        return plc.read(tag)
        #return plc.get_tag_list(program='*')


print(read_udt('HMI_IND'))
