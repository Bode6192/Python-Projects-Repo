# We time our code if we have multiple solutions to a particular
# problem and we're trying to find the fastst.


import time, timeit


def func_one(n):

    return [str(num) for num in range(n)]

print(func_one(10))


def func_two(n):

    return list(map(str, range(n)))

print(func_two(10))


print()


# For Function Two

# Current Time Before
start_time = time.time()

# Run Code
result = func_two(1000000)

# Current Time After Running Code
end_time = time.time()

# Elapsed Time
elapsed_time = end_time - start_time


print(elapsed_time)


print()


# For Function One

# Current Time Before
start_time = time.time()

# Run Code
result = func_one(1000000)

# Current Time After Running Code
end_time = time.time()

# Elapsed Time
elapsed_time = end_time - start_time


print(elapsed_time)



# USING THE TIMEIT MODULE

# For Function One

# this is the code that is run over and over again
stmt = '''
func_one(100)
'''

# Setup is basically what you have before the statement
setup = '''
def func_one(n):

    return [str(num) for num in range(n)]
'''

print()

print(timeit.timeit(stmt, setup, number=100000))


# For Function Two

# this is the code that is run over and over again
stmt = '''
func_two(100)
'''

# Setup is basically what you have before the statement
setup = '''
def func_two(n):

    return [str(num) for num in range(n)]
'''

print()

print(timeit.timeit(stmt, setup, number=100000))



