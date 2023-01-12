# Write a function that capitalizes the first and fourth letters of a name


def main():
    def old_macdonald(name='macdonald'):
        print(name[0].upper() + name[1:3].lower() + name[3].upper() + name[4:].lower())

    old_macdonald()

if __name__ == "__main__":
    main()


