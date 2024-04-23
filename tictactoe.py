# def board_display(board):
#     return print(board)

# game menu
def start_game(start, name, display_name, first_move):
    return start, name, display_name, first_move


# def decisions():
#     pass



# board display
# board_vertical_lines_1 = ('      |  |\n   ----------\n      |  |\n   ----------\n      |  |\n')
# board_display(board_vertical_lines_1)


# start game variables
welcome = print('Welcome to Tic Tac Toe')
user_name = input('What is your username? ')
your_name = print(f'Your name is {user_name}!')
first_or_second = input('Would you like to go first or second? ').lower
start_game(welcome, user_name, your_name, first_or_second)