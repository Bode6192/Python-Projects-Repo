# A function that takes a two-word string and returns True if both words begin with the same letter


def main():
    def animal_crackers(word):
        if word.split(" "):
            splits = word.upper().split(' ')
            if splits[0][0] == splits[1][0]:
                print(True)
                return True
            else:
                print(False)
                return False
            
        else:
            print('Not a two string word')


    animal_crackers('lama lock')


if __name__ == "__main__":
    main()