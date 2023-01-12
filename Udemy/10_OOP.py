class Dog():

    # CLASSS OBJECT ATTRIBUTE
    species = 'mammal'

    # OBJECT ATTRIBUTE
    def __init__(self, name, spots, breed):
        
        self.name = name

        # EXPECTS A BOOLEAN
        self.spots = spots

        self.breed  = breed

    def bark(self, number):
        return 'WOOF!!! '* number + f'My name is {self.name}'


my_dog = Dog( breed='Lab', name='Henry', spots=False)

print(my_dog.bark(3))



print()



class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 22/7

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        return Circle.pi * self.radius * 2

    def get_area(self):
        return Circle.pi * (self.radius)**2



my_circle = Circle(30)

print(my_circle.get_area())
print(my_circle.get_circumference())