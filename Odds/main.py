# Odds Numbers
# This program ask the user for 2 numbers, then
# it shows all the odds between this 2


def odd_number(x1: int, x2: int):
    """Calculate the odds between 2 given numbers"""

    # Sort the limits
    if x1 > x2:
        max_limit = x1
        min_limit = x2
    elif x2 > x1:
        max_limit = x2
        min_limit = x1
    else:
        return "There's not odd numbers between this 2"

    odd_list = []
    while min_limit <= max_limit:
        if min_limit % 2 != 0:
            odd_list.append(min_limit)
        min_limit += 1

    return odd_list


if __name__ == '__main__':
    print('*' * 15)
    print('ODDS NUMBERS')
    print('*' * 15)

    number_1 = int(input('Give me a number: '))
    number_2 = int(input('Give me a another: '))

    result = odd_number(number_1, number_2)

    print(result)
