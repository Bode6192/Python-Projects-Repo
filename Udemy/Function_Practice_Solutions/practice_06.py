# Given a sentence, return the sentence reversed

def main():
    def master_yoda(sentence):
        reverse = sentence.split(' ')
        list_reverse = reverse[::-1]
        print(' '.join(list_reverse))
        return ' '.join(list_reverse)

    Sentence = input('Please enter  sentence: ')
    master_yoda(Sentence)

if __name__ == "__main__":
    main()
