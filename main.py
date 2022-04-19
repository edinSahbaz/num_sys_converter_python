from util.convert_num import convert_num
from util.user_input import *


# Header
print('\n\nNumber system converter')
print('-----------------------')


# Number systems and number - USER INPUT
num_sys_convert_from = input_num_sys(
    '\nEnter a number system to convert from: ')
num_sys_convert_into = input_num_sys(
    '\nEnter a number system to convert into: ')
number = input_num(num_sys_convert_from)


# Convert number from one system to another
converted_number = convert_num(
    number, num_sys_convert_from, num_sys_convert_into)


# Output of converted number
print(f'\n\n{num_sys_convert_from.capitalize()} number "{number}" is equal to number "{converted_number}" in {num_sys_convert_into}.\n')
