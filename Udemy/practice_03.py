# To print out the lesser of two even numbers if both are even, 
# else returns the greater if one is odd
def main():

    def lesser_of_two_even(a,b):
        a = int(input("Input the value of A: "))
        b = int(input("Input the value of B: "))

        if (a % 2 == 0) and (b % 2 ==  0):
            print(min(a,b))
        else:
            print(max(a,b))

    lesser_of_two_even(2,4)

if __name__ == "__main__":
    main()

