# SPYGAME

# Write a function that takes in a list of integers and returns True if it contains 007 in order


def main():
    def spy_game(list1):
        for i in range(len(list1)):
            if (list1[i] == 0):
                list2 = list1[i+1:]
                for i in range(len(list2)):
                    if (list2[i] == 0):
                        list3 = list2[i+1:]
                        for i in range(len(list3)):
                            if (list2[i] == 7):
                                print(True)
                                return True
                            else:
                                print(False)
                                return False
                    else:
                        print(False)
                        return False
            else:
                print(False)
                return False

    

    list1 = [1,7,2,0,4,5,0]
    spy_game(list1)

if __name__ == '__main__':
    main()