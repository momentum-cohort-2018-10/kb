def is_power_of(number, base):
    """
    Given a number and a possible base, see if the number is a multiple of that base.
    """
    # print("number", number)
    # print("base", base)
    # if number == base:
    #     return True
    # elif number < 1:
    #     return False
    # else:
    #     return is_power_of(number / base, base)

    while number > base:
        number = number / base
    if number == base:
        return True
    else:
        return False


print(is_power_of(64, 2))
print(is_power_of(18, 3))
