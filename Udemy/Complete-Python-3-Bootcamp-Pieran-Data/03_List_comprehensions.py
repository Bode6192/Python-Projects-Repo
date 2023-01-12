my_list = [num for num in range(0, 100, 2)]
print(my_list)

celsius = [32, 46, 82, 73, 64]

Fahrenheit = [((9/5)*temp + 32) for temp in celsius]

print()

print(Fahrenheit)

my_list2 = [x*y for x in [2,4,6] for y in [10, 100, 1000]]

print(my_list2)

