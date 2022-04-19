from util.conversions.convert_to_decimal import convert_to_decimal


def convert_to_hexadecimal(num, num_sys):
    output = ''

    if num_sys == 'binary':
        num = convert_to_decimal(num, num_sys)

    num = int(num)
    digits_array = []

    while num != 0:
        num = num / 16
        digit = (num - int(num)) * 16
        num = int(num)

        digits_array.append(str(int(digit)))

    i = 0
    for digit in digits_array:
        if digit == '10':
            digits_array[i] = 'A'

        elif digit == '11':
            digits_array[i] = 'B'

        elif digit == '12':
            digits_array[i] = 'C'

        elif digit == '13':
            digits_array[i] = 'D'

        elif digit == '14':
            digits_array[i] = 'E'

        elif digit == '15':
            digits_array[i] = 'F'

        i += 1

    digits_array.reverse()

    for el in digits_array:
        output += el

    return output
