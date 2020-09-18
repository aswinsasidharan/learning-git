#library import and global variables
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}




#Card class

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value= values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'


#Deck class

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        #create all cards in the deck
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
        
    def deal_one(self):
        return self.all_cards.pop(0)
        
    def __str__(self):
        return f'No of cards in the deck is {len(self.all_cards)}'
    
                
            
#Player Class

class Hand():
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,newcard):
        self.cards.append(newcard)
        self.value = (self.value + newcard.value)
        
        
        if newcard.suit == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        self.value = self.value - 10
        


#Chips class

class Chips:
    
    def __init__(self):


        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total = self.total + (self.bet*0.5)
        self.bet = 0
    
    def lose_bet(self):
        self.total = self.total - self.bet
        self.bet = 0
        
    def push(self):
        self.total = self.total
        self.bet = 0
        
    def __str__(self):
        return f"Your current balance is {self.total} chips"


#function for taking bet

def go_bet(chip):
    
    while chip.total > 0 :
        
        try:
            chip.bet= int(input("Enter how much you want to bet :"))
        except:
            print("Enter a valid bet amount!!")
            
        else:
            
            if chip.bet <= chip.total:
                
                print(f"Your bet of amount {chip.bet} has been raised.. Wishing You Luck")
                break
            elif chip.bet > chip.total:
                print(f"Sorry insufficient balance!!! \nYour current balance is {chip.total} ")
                continue
                
    if chip.total == 0:
        print("Sorry Your Balance is Zero")



#function for performing hit

def hit(deck,hand):
    hand.add_card(deck.deal_one())
    


#hit or stand

def hit_or_stand(deck,hand):
    
    while PlayerHand.value < 21:
        
        
        
        decision = input("Do you want to hit(Press'H') or stand(Press 'S')")
        if decision not in ['H','S']:
            continue
        elif decision == 'H':
            hit(deck,hand)
            print('\n'*100)
            showsome(PlayerHand,DealerHand)
            continue 
            
        elif decision == 'S':
            break



#functions to display
def showsome(player,dealer):
    print('The player cards are :\n')
    for card in player.cards:
        print(f'{card} | ')
    print(f'Total value = {player.value}')
        
    print('Dealer :\n')    
    num = len(dealer.cards)
    while num-1 > 0:
        print(f'{dealer.cards[num-1]} | ')
        num -= 1
    if num-1 ==0:
        print("###########")



#function to display at the end

def show_all(player,dealer):
    print('The player cards are :\n')
    for card in player.cards:
        print(f'{card} | ')
    print(f'Total value = {player.value}')
    
   
    print('The Dealer cards are :\n')
    for card in dealer.cards:
        print(f'{card} | ')
    print(f'Total value = {dealer.value}')




#end game functions 
def player_busts(chip):
    print("BUSTED!!!\nValue exceeded 21")
    chip.lose_bet()
    

def player_wins(chip):
    
    print("YOU WON!!!")
    chip.win_bet()
    
     

def dealer_busts(chip):
    
    print("YOU WON!!!\nDealer Busted")
    chip.win_bet()
    
def dealer_wins(chip):
    
    print("SORRY YOU LOST!!!")
    chip.lose_bet()
    
def pushed(chip):
    
    print("THAT'S A TIE....PUSH")
    chip.push()    


#GAME PLAY

#opening statements
print("WELCOME TO THE BLACKJACK")
 #creating deck and dealing two cards to each player

PlayerChips = Chips()
blackjack= True
while blackjack== True:
    
    while True:
        begin = input("Would You Like To Begin(Y/N)?")
        if begin == 'Y':
            print("The game starts now....")
            break
        elif begin == 'N':
            print("Game play terminated....")
            continue
        else:
            print("Please type Y or N..")
            continue


  #creating deck and dealing two cards to each player
    PlayDeck = Deck()
    PlayDeck.shuffle()
    print("Deck Created and Shuffled")

    PlayerHand = Hand()
    DealerHand = Hand()

    for num in range(0,2):
        PlayerHand.add_card(PlayDeck.deal_one())
        DealerHand.add_card(PlayDeck.deal_one())


    #PlayerChips = Chips()
    print("Two cards are dealt and your chips are Ready")
    print(f"You Have {PlayerChips.total} chips to bet....")

    #prompting to bet and displaying the 2 cards with one dealer card hidden
    go_bet(PlayerChips)


    print('\n'*100)
    showsome(PlayerHand,DealerHand)

    playerturn = True
    while playerturn == True:
        
        hit_or_stand(PlayDeck,PlayerHand)
        

        if PlayerHand.value == 21:
            print("BLACKJACK")
            player_wins(PlayerChips)
            break
        elif PlayerHand.value > 21:
            player_busts(PlayerChips)
            break

        playerturn = False

        

        

    #Dealer turn begins
    else:

        while DealerHand.value < 17:
            hit(PlayDeck,DealerHand)

        print("\n"*100)
        show_all(PlayerHand,DealerHand)

        if DealerHand.value > 21:
            dealer_busts(PlayerChips)

        elif DealerHand.value < PlayerHand.value:
            player_wins(PlayerChips)

        elif DealerHand.value > PlayerHand.value:
            dealer_wins(PlayerChips)

        elif  DealerHand.value == PlayerHand.value:
            pushed(PlayerChips)
    
    #game ended and asking whether to play again or not
    print(PlayerChips)
    
    if PlayerChips.total > 0:
        while True:
            decide = input("Would You Like to Play Again?(Y/N)")
            if decide == 'Y':
                blackjack = True
                break
            elif decide == 'N':
                blackjack= False
                break
            else :
                print("Please type Y or N....")
                continue
    else:
        print("Sorry You Have to Pay to Play Again due to Zero balance")
        blackjack= False
        
        