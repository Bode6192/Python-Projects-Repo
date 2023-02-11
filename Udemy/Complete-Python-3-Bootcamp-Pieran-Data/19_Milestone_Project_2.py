# Black Jack Game


import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 
          'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += card.__str__() + '\n' 
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    
    def __init__(self):
        self.cards = []   # start with an empty list
        self.value = 0    # start with zero value
        self.aces = 0     # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1
        self.value += card.value

    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self, total):
        self.total = total    # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many would you like to bet? '))
        except ValueError:
            print('Oops! Please enter digit characters')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have {chips.total}')
            else:
                break


def hit(deck, hand):

    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    
    global playing      # to control an upcoming while loop

    choice = None
    while (choice != 'H') and (choice != 'S'):
        choice = input('Do you want to hit or stand? Enter(H or S) ').upper()

    if choice == 'H':
        hit(deck, hand)
    else:
        print("Player stands, Dealers's Turn")
        playing = False


def show_some(player, dealer):

    # Show only one of the dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # Show all (2 cards) of the player's hand/cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):

    # Show all the dealer's cards
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)

    # calculate and display value (J+K == 20)
    print(f"Value of dealer's hand is {dealer.value}")

    # Show all of the player's hand/cards
    print("\nPlayer's Hand: ", *player.cards, sep = '\n')
    print(f"Value of player's hand is {player.value}")


def player_busts(player, dealer, player_chips):

    print('BUST Player!!!')
    player_chips.lose_bet()

def player_wins(player, dealer, player_chips):

    print('Congratulations Player!!! You win')
    player_chips.win_bet()


def dealer_busts(player, dealer, player_chips):

    print('BUST Dealer!!!')
    player_chips.win_bet()


def dealer_wins(player, dealer, player_chips):

    print('Congratulations Dealer!!! You win')
    player_chips.lose_bet()


def push(player, dealer):

    print('Dealer and player tie! PUSH')



# GAME LOGIC

while True:
    # Print an opening statement

    print('WELCOME TO BLACKJACK')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    total = 0
    while total < 1:
        total = int(input('Please enter a valid number of Chips: '))

    player_chips = Chips(total)

    
    # Prompt the Player for their bet
    take_bet(player_chips)


    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)


    while playing:      # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)


        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)


        # If player's hand exceeds 21, run player_busts() and break out of the loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If player hasn't busted, play dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards 
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print(f'\n Player total chips are at: {player_chips.total}')

    # Ask to play again
    new_game = input('Would you like to play another hand? Enter Y or N: ')
    
    if new_game.upper() == 'Y':
        playing = True
        continue
    else:
        print('Than you for playing!')
        break    


