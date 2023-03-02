import random


# Question 1
def gensquares(N):

    for i in range(N):
        yield i*2

for num in gensquares(10):
    print(num)


print()


# Question 2
def rand_num(low, high, n):

    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1, 10, 12):
    print(num)


print()


# Question 3
s = 'hello'

s_iter = iter(s)


print()


# Question 4
# We could use a yield statement in a function that an 
# iterable instead of creating a list then iterating over it


# Extra Credit
# gencomp = (item for item in my_list if item > 3)
# gencomp is a generator expression, which 
# is a compact and memory-efficient way to generate a list 
# comprehension in Python.  The items are generated one by 
# one on-the-fly as they are needed, rather than being stored 
# in memory all at once like in a list comprehension.


my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 3)

print(gencomp)






