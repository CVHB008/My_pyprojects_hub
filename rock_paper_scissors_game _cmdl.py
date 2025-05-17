import random as rand
import time as tt

#A menu driven Rock Paper Scissor game
error = False

player_score = 0
computer_score = 0

rules ='\nRules:\n1.First choose an option of your wish.\
\n2.Second the computer will choose its option.\
\n3.Based on both the choices the Winner will be selected and both\n\
of your scores will be kept in track and will be displayed in the end of every game.\n'

print('\n', 8 * '\t', 'Welcome To The Game ==> Rock Paper Scissors\n"Note : This is a 5 on 5 \
round and after completing 5 rounds you can choose to continue playing or quit"')
print()


def get_choices():
    
    choice = ['rock','paper','scissor']
    player_choice = input("\n\nEnter your choice(rock,paper,scissor):").lower()
    computer_choice = rand.choice(choice)
    choices = {'player' : player_choice,'computer' : computer_choice}
    return choices

def who_is_winner(player,computer):
    global player_score
    global computer_score
    global error
    if player.lower() in ['rock', 'paper', 'scissor']:
        print(f'You chose : {player}\nComputer chose : {computer}')
    if computer == player:
        player_score += 1
        computer_score += 1
        return "It's a Tie match"
    
    elif player == 'rock':
        if computer == 'paper':
            computer_score+=1
            return 'Paper catches the Rock, Computer wins the game'
        else:
            player_score += 1
            return 'Rock smashes the Scissor, You win the game'
            
    elif player == 'paper':
        if computer == 'scissor':
            computer_score += 1
            return 'Scissor cuts the Paper, Computer wins the game'
        else:
            player_score += 1
            return 'Paper catches the Rock, You win the game'
            
    elif player == 'scissor':
        if computer == 'Rock':
            computer_score += 1
            return 'Rock smashes the Scissor, Computer wins the game'
        else:
            player_score += 1
            return 'Scissor cuts the Paper, You win the game'
            
    else:
        error = True
        return "'INVALID Input'\nPlease Try Again"

def run():
    global error

    n = 1
    while n <= 5:
        choices = get_choices()
        result = who_is_winner(choices['player'], choices['computer'])
        print(result)
        tt.sleep(0.1)
        if not error:
            n += 1
        else:
            error = False

    play = input('\nDo you want to play again(Y/N) : ')
    print()
    if play.upper() == 'Y':
        run()
    elif play.upper() == 'N':
        menu()
    else:
        print('INVALID INPUT')
        tt.sleep(0.1)
        menu()


def menu():
    print('Menu\n1.Game Rules\n2.Play Game\n3.Quit Game\n4.Display score board')
    try:
        option = int(input('Enter the option : '))

    except ValueError:
        menu()

    if option == 1:
        print(rules)
        tt.sleep(0.1)
        menu()
        
    elif option == 2:
        run()
            
    elif option == 3:
        if player_score ==0 and computer_score == 0:
            print('See you next time')
            tt.sleep(2)
        else:
            if player_score == computer_score:
                print('\nIt seems to be a tie match today')
            else:
                tt.sleep(0.1)
                print(f'\nScore Board :\nYour score : {player_score}\nComputer Score : {computer_score}')
                
                if player_score > computer_score:
                    print('\nIt seems this is your lucky day, You are the Winner')
                else:
                    print('Well played, Better luck next time')
                    
            print('THANKYOU FOR PLAYING, COME AGAIN')
            tt.sleep(5)
        
    elif option == 4:
        tt.sleep(0.1)
        print(f'\nScore Board :\nYour score : {player_score}\nComputer Score : {computer_score}\n')
        menu()
        
    else:
        print('Enter a valid option please')
        tt.sleep(0.1)
        menu()

menu()
