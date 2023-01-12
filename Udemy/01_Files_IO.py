with open('myfile.txt', 'w') as myfile:
    contents = myfile.write("Hello, my name is Gbenga Olabode, \nI love fried rice") 

myfile = open('myfile.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.read())

myfile.close()
