# Given a string, return a string where for every character in the original there are three characters

def main():
    def paper_doll(word):
        list1 = []
        for letter in word:
            multiple = 3*letter
            list1.append(multiple)
        print(', '.join(list1))
        return ''.join(list1)

    word = input('Please enter a word to multiply:  ')
    paper_doll(word)
            


if __name__ == '__main__':
    main()