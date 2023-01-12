# def myfunc(a, b):
#     return sum((a, b)) 
# x = 40
# y = 60
# print(myfunc(x, y))

# print(help(sum))

def myfunc(args):
    output = []
    for letter_pos in range(len(args)):
        if letter_pos % 2 == 0: 
            output.append(args[letter_pos].upper())
        elif letter_pos % 2 != 0:
            output.append(args[letter_pos].lower())
    return ''.join(output)

name = 'Gbenga'

print(myfunc(name))

def say_hello():
    print('Hello how are you?')

say_hello()
print(myfunc(name))


