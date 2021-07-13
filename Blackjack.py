import random

print('****************************************')
print("* Welcome to Daniel's Casino game v1.0 *")
print('*  started on 11/18/2020 using Python  *')
print ('****************************************')
print ('')
    



def new_deck():
    '''creates a new 52 card deck
    '''
    deck = []
    for suit in ('H', 'D', 'C', 'S'):
        for rank in ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'):
            deck.append(suit + rank)
    return deck

def shuffle(deck):
    random.shuffle(deck)
    return deck

def card_values():
    """Generates Values of all cards, giving aces 11
    """
    deck = new_deck()
    values = {}
    for card in deck:
##        print card
        for i in range(13):
            
            for rank in card:
                if rank == '1':
                    values[card] = 10
                    
                elif rank == str(i) and rank != '1' and rank != '0':
                    values[card] = i

                elif rank == 'J' or rank == 'Q' or rank == 'K':
                    values[card] = 10

                elif rank == 'A':
                    values[card] = 11  
    return values


def new_hand(deck):
    """Deals hand to player and dealer and lets player take turn
    """
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(deck[0])
        deck.remove(deck[0])
        dealer_hand.append(deck[0])
        deck.remove(deck[0])

    user_input = ''
    print('__________________________')
    print ('The Dealer has:', dealer_hand[0], '|', '??', '(',values[dealer_hand[0]], '+ ?? )')
    print ('')
    print ('Your hand is: ', player_hand, '(', hand_value(player_hand), ')')
    print ('')
    while True:
        if hand_value(player_hand) == 21:
            print ('B L A C K J A C K ')
            break
        elif hand_value(player_hand) > 21:
            print ('You bust!')
            break
        else:
            print ('Select From The Following....')
            print ('(H) Hit ')
            print ('(S) Stand ')
            user_input = input('What is your selection? ')
            if user_input == 'H' or user_input =='h':
                print ('')
                print ('You recieve: ', deck[0])
                player_hand.append(deck[0])
                deck.remove(deck[0])
                print ('Your Hand is', player_hand, hand_value(player_hand))
                print ('')
               
            else:
                print ('You end your turn with: ', hand_value(player_hand))
                break


        
    return player_hand, dealer_hand


def dealer_plays(dealer_hand, deck):
    """Dealer plays hand according to rules of blackjack
    """
    print ('')
    print ("The Dealer's Cards Are: ", dealer_hand, hand_value(dealer_hand))
    while hand_value(dealer_hand) < 17:
##        print 'The dealer ends its turn with: ', hand_value(dealer_hand)
        print ('The Dealer hits')
        print ('')
        print ('The Dealer gets', deck[0])
        dealer_hand.append(deck[0])
        deck.remove(deck[0])
        print ("The Dealer's Cards Are: ", dealer_hand, hand_value(dealer_hand))
        if hand_value(dealer_hand) > 21:
            print ('The Dealer Busts.')
            return 
    print ('The Dealer ends its turn with:', hand_value(dealer_hand))

                    
def hand_value(hand):
    """ calculates value of a given hand and returns that value
    """
    hand_value = 0
    for card in hand:
        hand_value = hand_value + values[card]
    for card in hand:
        if values[card] == 11 and hand_value > 21:
            hand_value = hand_value - 10
            
    return hand_value



    
def blackjack():
    print ('Welcome to Blackjack')
    print ('')
    deck = shuffle(new_deck())
    while True:
        if len(deck) < 20:
            deck = shuffle(new_deck())
            print ('Reshuffling Deck...')
            print ('')
        else:
            print ("Enter Y to play a game or E to exit")
            answer = input('')
            if answer == 'Y' or answer == 'y':
                player_hand, dealer_hand = new_hand(deck)
                if hand_value(player_hand)> 21:
                    print ("Dealer Wins")
                    ## If player bust, asks if you want to play another hand. Otherwise dealer plays
                else:
                    dealer_plays(dealer_hand, deck)
                    if hand_value(dealer_hand) > 21:
                        print ('You Win')
                    
                    elif hand_value(dealer_hand) == hand_value(player_hand):
                        print ("Push") #If tie with no bust)
                        print ('You get your wager back')
                        
                    elif hand_value(player_hand) > hand_value(dealer_hand):
                        print ('Player Wins') # Since loop resets if player busts, its safe to say
                                            # that Player wins if player score > dealer score

                    else:
                        print ('Dealer Wins') # If Player Didn't win.....

            elif answer == 'E' or answer == 'e':
                print ('Thanks for playing.')
                break;

                
            else:
                print ('Invalid input, please try again' )

        
   
values = card_values()
blackjack()


##game_selection = ''
##while game_selection == '':
##    print 'Please choose between the following options;'
##    print ' (B) | Play Blackjack '
##    print ''
##    print ' (C) | Check your balance '
##    print ' (E) | Exit the Casino'
##
##    game_selection = raw_input('What is your selection?')
##    if game_selection == 'B' or game_selection == 'b':
##        blackjack()
##    elif game_selection == 'E' or game_selection == 'e':
##        print 'Thanks for playing'
##    elif game_selection == 'C' or game_selection == 'c':
##        print 'Feature coming soon...'
##    else:
##        print ''
##        print 'Invalid Selection, Please Try Again '
##        print ''
##        game_selection = ''
