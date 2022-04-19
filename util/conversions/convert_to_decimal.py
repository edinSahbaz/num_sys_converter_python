import numpy
from util.check_num import hexadecimal


def conversion(num, base, isHex=False):
    index = 0
    output = 0

    # If num is hexadecimal replace letters with numbers for conversion
    if isHex:
        num = list(num)
        i = 0

        for digit in num:
            if digit == 'A':
                num[i] = '10'

            elif digit == 'B':
                num[i] = '11'

            elif digit == 'C':
                num[i] = '12'

            elif digit == 'D':
                num[i] = '13'

            elif digit == 'E':
                num[i] = '14'

            elif digit == 'F':
                num[i] = '15'

            i += 1

    for digit in num[::-1]:
        output += int(digit) * (base ** index)
        index += 1

    return output


def convert_to_decimal(num, num_sys):
    output = 0

    if num_sys == 'binary':
        output = conversion(num, 2)

    else:
        output = conversion(num, 16, True)

    return output
