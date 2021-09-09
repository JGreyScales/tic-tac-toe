import os, time

# dict's
board = [['?1', '?2', '?3'], ['?4', '?5', '?6'],
['?7', '?8', '?9']]
values = ["X", "O"]
win_combos = ['123', '456', '789', '147', '258', '369', '159', '357']
null = []
player_vs_player = True


# "framerate" on the board, updates the display
def board_update(board):
    os.system('cls')
    print(f'\n' * 5)
    for item in board:
        print(", ".join(item))

def win_check(board, player):

    win_numbers_true = ""
    win_numbers = ""

    # gathers all squares the player currently owns
    for row in board:
        for column in row:
            if column[0] == player:
                win_numbers += column[1]

    # checks if player has less then 3 tallies on the board
    if len(win_numbers) < 3:
        win_numbers = ""
        return False

    else:
        #checks if player made a quick win (to save proccessing time later on)
        if win_numbers in win_combos:
            return True
        else:
            ## gathers all squares that are apart of combos and are player controlled and sees if they have enough to make a combo
            for combo in win_combos:
                for letter in win_numbers:
                    if letter in combo:
                        win_numbers_true += letter

                if win_numbers_true in win_combos:
                    return True
                win_numbers_true = ""
    win_numbers = ""
    return False

def gameloop():
    global board
    if player_vs_player == True:
        # runs the game twice for each human player
        for player in values:
            player_turn = True
            # while the user hasnt done a valid turn / is still their turn
            while player_turn == True:
                # board init/refresh
                board_update(board)
                print('What spot would you like to fill?')
                print(f'player: {player}\'s turn')
                user_choice = int(input(f'\n' * 2))

                ## goes by each row then each column in each row and checks if the spot they are trying to edit is valid / what spot to change
                row_count = 0
                column_count = 0
                for row in board:

                    for column in row:
                        
                        ## if the column (spot on board) == the users desired spot
                        if int(column[1]) == user_choice:
                            # if board[row][column][fist letter] != ? then the spot has already been picked
                            if board[row_count][column_count][0] != "?":
                                print('that spot is already taken')
                                time.sleep(2)
                                board_update(board)
                            # else the spot is free and convert that spot to the players
                            else:
                                board[row_count][column_count] = f'{player}{board[row_count][column_count][1]}'
                                player_turn = False

                        column_count += 1
                    column_count = 0
                    row_count += 1


            if win_check(board, player) == True:
                print(f'player: {player} has won!')
                return
            
            board_update(board)
    gameloop()
gameloop()