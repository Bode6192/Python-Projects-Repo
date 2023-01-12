# Given a list of ints, return True if the array contains a 3 next
# to a 3 somewhere

def has_33(list_values):
    for num in range(len(list_values)):
        if list_values[num] == 3 and list_values[num+1] == 3:
            print(True)
            return True
    else:
        print(False)
        return False

has_33([1, 3, 3])