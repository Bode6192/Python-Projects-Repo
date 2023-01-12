word = 'abcde'

for item in enumerate(word):
    print(item)

for index,letter in enumerate(word):
    print(f'Index {index} has a value {letter}')

mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300, 400, 500]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

print(list(zip(mylist1, mylist2)))

from random import shuffle

shuffle(mylist1)
print(mylist1)

from random import randint
rand_num = randint(0, 100)
print(rand_num)