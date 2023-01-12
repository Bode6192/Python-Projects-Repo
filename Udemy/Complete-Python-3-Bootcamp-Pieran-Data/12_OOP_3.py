# In Polymorphism different classes share the same method
# Therefore we can call these methods without worrying about
# the classes we use to call said method


class Book():
    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    #  SPECIAL METHODS
    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f'{self.title} has been deleted from object memory')
    

my_book = Book('Python rocks', 'Gbenga', 420)

print(my_book)
print(len(my_book))

print()

del my_book