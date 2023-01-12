import pprint

# To store the values 
# for the amount of times a character in message appears. 

message = '''It was a bright cold day in April,
and the clocks were striking thirteen'''

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

string_val = pprint.pformat(count)
print(string_val)

# To get the value for the key 'a' in the count Dictionary 
print(count.get('a', 0))