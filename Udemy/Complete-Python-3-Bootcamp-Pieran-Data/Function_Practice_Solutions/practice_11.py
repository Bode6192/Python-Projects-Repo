# SUMMER of 69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 or no numbers

def main():
    
    def summer_90(list1):
        sum = 0
        for i in list1:
            if i == 6 or i == 7 or i == 8 or i == 9:
                continue
            else:
                sum += i
                
        print(sum)
        return sum

    your_list = [2, 1, 6, 9, 11]
    summer_90(your_list)

if __name__ == '__main__':
    main()


