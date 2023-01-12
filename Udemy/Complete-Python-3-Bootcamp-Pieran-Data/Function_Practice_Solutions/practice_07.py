# Given an integer n, return True if n is within 10 of either 100 or 200

def main():
    def almost_there(number):
        if abs(number-100)< 10 or abs(number-200) < 10:
            print(True)
            return True
        else:
            print('Number not within 10 of either 100 or 200') 

    num = int(input('Enter an integer'))
    almost_there(num)


if __name__ == "__main__":
    main()