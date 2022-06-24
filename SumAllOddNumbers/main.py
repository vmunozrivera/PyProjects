# Sum All Odd Numbers
# Print the sum of all odd numbers from a list

from functools import reduce


def sum_odd(my_list):
    odd_list = list(filter(lambda x: x % 2, my_list))
    print(odd_list)
    reduce_list = reduce(lambda a, b: a + b, odd_list)
    print(reduce_list)


new_list = [1, 2, 3, 4, 5]

sum_odd(new_list)
