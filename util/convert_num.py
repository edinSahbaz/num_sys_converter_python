from util.conversions.convert_to_binary import *
from util.conversions.convert_to_decimal import *
from util.conversions.convert_to_hexadecimal import *


def convert_num(num, num_sys_convert_from, num_sys_convert_into):
    if num_sys_convert_into == 'binary':
        return convert_to_binary(num, num_sys_convert_from)

    elif num_sys_convert_into == 'decimal':
        return convert_to_decimal(num, num_sys_convert_from)

    else:
        return convert_to_hexadecimal(num, num_sys_convert_from)
