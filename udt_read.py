from pycomm3 import LogixDriver


def read_udt(tag):
    with LogixDriver('10.160.8.13/0') as plc:
        print(plc.get_plc_info())
        return plc.read(tag)
        # return plc.get_tag_list(program='*')


print(read_udt('HMI_IND'))
