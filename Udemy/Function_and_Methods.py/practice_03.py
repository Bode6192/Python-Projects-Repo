# Write a Python function that takes a list and returns a new list
# with unique elements of the first list.

import numbers


def unique_list(lst):
    return list(set(lst))

sample_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]

print(unique_list(sample_list))

# Write a Python Function to multiply all the numbers in a list

num_list = [1, 2, 3, -4]

def multiply_list(numbers):
    output = 1
    for num in numbers:
        output *= num
    return output

print(multiply_list(num_list))