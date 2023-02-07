# Write a Func that returns the volume of a given radius

def vol(rad):
    print((4/3) * (22/7) * (rad)**3)
    return (4/3) * (22/7) * (rad)**3

vol(2)


# Write a Func that checks whether a number is in a given range
# (inclusive of high and low)

def ran_check(num, low, high):
    for number in range(low, high + 1):
        if num == number:
            print(f'Yes {num} is in the range of {low} to {high} both inclusive')
            return True
    else:
        print(f'False {num} is not in the range of {low} to {high} both inclusive')
        return False

print(ran_check(5,2,7))
