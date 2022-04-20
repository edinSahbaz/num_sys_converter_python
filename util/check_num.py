# Number systems
num_systems = ['binary', 'decimal', 'hexadecimal']
binary = ['0', '1']
decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
hexadecimal = ['0', '1', '2', '3', '4', '5', '6',
               '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# Check if number is valid
def validate_num(num, digits):
    is_valid = True

    for digit in num:
        if not digit in digits:
            is_valid = False
            break

    return is_valid


# Check if number belogns to number system
def check_num(num, num_sys):
    if num_sys in num_systems:
        if num_sys == 'binary':
            return validate_num(num, binary)

        elif num_sys == 'decimal':
            return validate_num(num, decimal)

        else:
            return validate_num(num, hexadecimal)

    else:
        return None
