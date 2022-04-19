from util.conversions.convert_to_decimal import convert_to_decimal


def convert_to_binary(num, num_sys):
    output = ''

    if num_sys == 'hexadecimal':
        num = convert_to_decimal(num, num_sys)

    num = int(num)

    while num != 0:
        if num % 2 == 0:
            output += '0'
        else:
            output += '1'

        num = num // 2

    if num_sys == 'hexadecimal' and len(output) % 4 != 0:
        output += '0' * (len(output) % 4)

    return output[::-1]
