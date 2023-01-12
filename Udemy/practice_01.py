def main():
    name = input("What is your name? ")
    hello(name)

def hello(to="world"):
    print('Hello,',to )

def square(n):
    return n * n

if __name__ == "__main__":
    main()
