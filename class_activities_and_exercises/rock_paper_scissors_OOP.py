import random
options_list = ['rock', 'paper', 'scissors']

#step 1: define the base class
class Player:
    def __init__(self,name):
        self.name = name

    def choose_move(self):
        pass

#step 2: create a derived class (HumanPlayer)
class HumanPlayer(Player):
    def choose_move(self):
        move = input(f'{self.name}, enter your move (rock, paper, scissors): ').lower()
        while move not in options_list:
            print('invalid move. please select rock, paper, or scissors.')
            move = input(f'{self.name}, enter your move (rock, paper, scissors): ').lower()
        return move

#step 3: create another derived class (ComputerPlayer)
class ComputerPlayer(Player):
    def choose_move(self):
        return random.choice(options_list)

#step 4: create a game class to manage gameplay
class RPSGame:
    #create the characters
    def __init__(self):
        self.player1 = HumanPlayer('Player 1')
        self.player2 = ComputerPlayer('Computer')
    def determine_winner(self,move1,move2):
        if move1 == move2:
            return "it's a tie!"
        elif (move1 == 'rock' and move2 == 'scissors') or \
            (move1 == 'scissors' and move2 == 'paper') or \
            (move1 == 'paper' and move2 == 'rock'):
            return f'{self.player1.name} wins!'
        else:
            return f'{self.player2.name} wins!'
    def play_game(self):
        #intro
        print('welcome to rock paper scissors!')
        #call the choose move method on player 1 and 2
        move1 = self.player1.choose_move()
        move2 = self.player2.choose_move()
        #inform the player the moves
        print(f'{self.player1.name} chose {move1}...')
        print(f'{self.player2.name} chose {move2}...')

        result = self.determine_winner(move1,move2)
        print(result)

#step 5: instantiate the game class
if __name__ == '__main__':
    game = RPSGame()
    game.play_game()