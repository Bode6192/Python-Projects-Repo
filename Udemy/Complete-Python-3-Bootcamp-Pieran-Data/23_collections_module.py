# Counter Function

from collections import Counter

mylist = [1,1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,3]

# The Counter is like a specialised dictionary that keeps track 
# of unique values in a list.
print(Counter(mylist))
print()


mylist = ['a', 'a', 'a', 10, 10, 10, 10]

print(Counter(mylist))
print()


string = 'aaaabbbbddddmmeeww'

print(Counter(string))
print()


statement = '''How many times does each word show up in this 
sentence with a word'''

print(Counter(statement.split()))
print()


# defaultdict

from collections import defaultdict

# It'll return a entered default value when the wrong key is 
# called from a dictionary instead of giving an error.  

d = {'Correct': 100, 'wrong': 12}

d = defaultdict(lambda: 0)

print(d['WRONG KEY!'])
print()


# Named Tuple
# This is similar to constructing a class in OOP
from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(4,'husky', 'Sammy')

print(sammy)
