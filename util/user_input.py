from util.check_num import check_num, num_systems


# Input number system
def input_num_sys(phrase):
    num_sys = None

    while True:
        num_sys = input(phrase).lower()

        if num_sys in num_systems:
            break

        else:
            print(
                f'Wrong entry! Try again.\n"{num_sys}" is not found in our number system library.')

    return num_sys


# Input number to convert
def input_num(num_sys_convert_from):
    num = None

    while True:
        num = input(
            f'\nEnter a {num_sys_convert_from} number: ')

        is_valid_num = check_num(num, num_sys_convert_from)

        if is_valid_num:
            break
        else:
            print(
                f'Wrong entry! Try again.\n"{num}" is not a {num_sys_convert_from} number.')

    return num
