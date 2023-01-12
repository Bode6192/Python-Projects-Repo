# Blackjack - Given three integers between 1 and 11,
# if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum(even after adjustments) exceeds 21, return 'BUST'

def main():
    def blackjack(a,b,c):
        if 1<a<=11 and 1<b<=11 and 1<c<=11:
            if a+b+c <= 21:
                print(a+b+c)
            elif (a+b+c > 21) and (a == 11 or b == 11 or c == 11):
                print((a+b+c) - 10)
            elif a+b+c > 21:
                print('BUST')
                

        else:
            print('All numbers entered not between 1 and 11')

    A = int(input('Enter a value for a'))
    B = int(input('Enter a value for b'))
    C = int(input('Enter a value for c'))
    blackjack(A,B,C)


if __name__ == '__main__':
    main() 