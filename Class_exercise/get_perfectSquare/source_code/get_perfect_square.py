import math

def get_perfect_squares(my_list):
    if not isinstance(my_list, list):
        raise ValueError("Can only be list")

    for digit in my_list:
        if isinstance(digit,float):
            raise ValueError("Can only be integer")
        elif isinstance(digit,str):
            raise ValueError("Can only be integer")
        elif not digit:
            raise ValueError("List can not be empty")
    new_list = []
    for numbers in my_list:
        number = int(math.sqrt(numbers))
        if number * number == numbers:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list


print(get_perfect_squares([2,3,4,9,6,25]))