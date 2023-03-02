def create_cubes(n):

    for num in range(n):
        yield num**3

create_cubes(10)

print()

for val in create_cubes(10):
    print(val)

print()

def gen_fibon(n):

    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a+b


for number in gen_fibon():
    print(number)


# The next() function generates the next value for (the first
# value) or (the next value after the last value called)
# The iter() function allows us to iterate over an iterable 
# that's not iterative 