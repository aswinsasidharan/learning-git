from IPython.display import clear_output
from random import randint


def display(test_board):
    clear_output()
    print(test_board[0]+' | '+test_board[1]+' | '+test_board[2])
    print('--|---|--')
    print(test_board[3]+' | '+test_board[4]+' | '+test_board[5])
    print('--|---|--')
    print(test_board[6]+' | '+test_board[7]+' | '+test_board[8])
    
 def player_marker_choice():
    marker = 'wrong'
    while (marker not in ['X','O'] ):
        
        marker = input("Player1 please choose your marker : X or O: ")
        
        player1 = marker
        if marker not in ['X','O']:
            print('Sorry,Invalid selection!!')
        

        elif player1 == 'X':
            player2 = 'O'
            print('Player1: X  Player2: O' )
    

        elif player1 == 'O':
            print('Player1: O  Player2: X' )
            player2='X'
        
    return(player1,player2)



def markorder():
    toss=''
    while toss != 'Y':
        
        toss=input("Shall we begin with toss...press Y to begin")
        
        if toss != 'Y':
            print("waiting for your reply...")
    order = randint(1,2)
    if order == 1:
        print("Player1 won the toss and can begin :")
        mark = player1
        
    else:
        print("Player2 won the toss and can begin :")
        mark = player2
    return mark


def poschooser(board):
    posn = 10
    while posn not in range(1,10) or board[posn-1]!=' ':
        
        posn =int(input("Choose the position: "))
        if posn not in range(1,10) or board[posn-1]!=' ':
            print('invalid choice')
    return posn
 


 def placemarker(board,mark,position):
    board[position-1] = mark
    
    
    return board




def endgame(board):
    
    if (board[0]==board[1]==board[2]==player1 or board[3]==board[4]==board[5]==player1 or board[6]==board[7]==board[8]==player1
          or board[0]==board[3]==board[6]==player1 or board[1]==board[4]==board[7]==player1 or board[2]==board[5]==board[8]==player1
          or board[0]==board[4]==board[8]==player1 or board[2]==board[4]==board[6]==player1 ):
        return 'Winner is Player1'
    elif (board[0]==board[1]==board[2]==player2 or board[3]==board[4]==board[5]==player2 or board[6]==board[7]==board[8]==player2
          or board[0]==board[3]==board[6]==player2 or board[1]==board[4]==board[7]==player2 or board[2]==board[5]==board[8]==player2
          or board[0]==board[4]==board[8]==player2 or board[2]==board[4]==board[6]==player2 ):
        return 'Winner is Player2'
        
        
        
    elif ' ' not in board:
        
        return 'End of Game..Game tied'
    else:
        return False


def gameon_choice():
    
    decision = 'wrong'
    
    while decision not in ['Y','N']:
        
        decision = input('Continue playing?  Y/N: ')
        
        if decision not in ['Y','N']:
            print('Sorry, I cannot understand..Choose Y or N')
            
    if decision== 'Y':
        return True
    else:
        return False




gameon = True
while gameon == True:
    board= [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display(board)
    player1,player2 = player_marker_choice()
    marking = markorder()
    end = False
    while end == False:
        
        if marking==player1 :
            print('\nPlayer1')
            posit = poschooser(board)
            board = placemarker(board,marking,posit)
            display(board)
            marking = player2
            end = endgame(board)
        else:
            print('\nPlayer2')
            posit = poschooser(board)
            board = placemarker(board,marking,posit)
            display(board)
            marking = player1
            end = endgame(board)
        
    final = endgame(board)
    print(final)
    gameon = gameon_choice()           