#python script from a QR code found in Cyberpunk 2077
import sys
from itertools import cycle

win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
optimal_moves = [4, 0, 2, 6, 8, 1, 3, 5, 7]

def check_win(board):
    for line in win_conditions:
        if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
            return board[line[0]]
    if ' ' not in board:
        return 'D'
    return None

def find_move(board, player):
    for move in optimal_moves:
        if board[move] == ' ':
            test_board = list(board)
            test_board[move] = player
            if check_win(test_board) == player:
                return move
    for move in optimal_moves:
        if board[move] == ' ':
            test_board = list(board)
            test_board[move] = 'X' if player == 'O' else 'O'
            if check_win(test_board) == ('X' if player == 'O' else 'O'):
                return move
    for move in optimal_moves:
        if board[move] == ' ':
            return move

def draw_board(board):
    print("\n 1 | 2 | 3      {} | {} | {}".format(*board[:3]))
    print("---+---+---    ---+---+---")
    print(" 4 | 5 | 6      {} | {} | {}".format(*board[3:6]))
    print("---+---+---    ---+---+---")
    print(" 7 | 8 | 9      {} | {} | {}".format(*board[6:]))

def game(num_games):
    games_played = 0
    while num_games == -1 or games_played < num_games:
        board = [' '] * 9
        for player in cycle('OX'):
            draw_board(board)
            move = find_move(list(board), player)
            board[move] = player
            win = check_win(board)
            if win:
                draw_board(board)
                if win == 'D':
                    print("Game over. Draw!")
                else:
                    print(f"Game over. {player} wins!")
                break
        games_played += 1
        if num_games != -1 and games_played >= num_games:
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_games = int(sys.argv[1])
    else:
        num_games = 1
    game(num_games)