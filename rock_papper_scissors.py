import random

def start():
    player = input('\nPlease, choose ROCK (R), PAPPER (P) or SCISSORS (S) and press \'enter\' to start\n').lower()
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return '\nNo winner. It is a TIE!\n'
    if is_win(player, computer):
        return '\nPlayer won. Congratulations!\n'

    return '\nComputer won! Try again =)\n'

def is_win(opponent1, opponent2):
    if(opponent1 == 'p' and opponent2 == 'r') or (opponent1 == 'r' and opponent2 == 's') or (opponent1 == 's' and opponent2 == 'p'):
        return True

print(start())