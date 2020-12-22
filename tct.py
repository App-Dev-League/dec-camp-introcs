# Implementation of Two Player Tic-Tac-Toe game in Python.


the_board = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in the_board:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the print_board function
    so that we can easily print the board everytime by calling this function. '''


def print_board(board):
    print(board['1'] + '  |  ' + board['2'] + '  |  ' + board['3'])
    print('–——  –——  –——')
    print(board['4'] + '  |  ' + board['5'] + '  |  ' + board['6'])
    print('–——  –——  –——')
    print(board['7'] + '  |  ' + board['8'] + '  |  ' + board['9'])

# Now we'll write the main function which has all the gameplay functionality.


def game():
    turn = 'X'
    count = 0
    for i in range(10):
        print_board(the_board)
        print("It's your turn, " + turn +
              ". Which place do you want to move to? ")
        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.")
            print()
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if the_board['1'] == the_board['2'] == the_board['3'] != ' ':  # across the top
                print_board(the_board)
                print()
                print("Game Over")
                print("" + turn + " won the game! Awesome job :)")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':  # across the middle
                print_board(the_board)
                print()
                print("Game Over")
                print("" + turn + " won the game! Awesome job :)")
                break
            elif the_board['7'] == the_board['8'] == the_board['9'] != ' ':  # across the bottom
                print_board(the_board)
                print()
                print("Game Over")
                print("" + turn + " won the game! Awesome job :)")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':  # down the left side
                print_board(the_board)
                print()
                print("Game Over")
                print("" + turn + " won the game! Awesome job :)")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':  # down the middle
                print_board(the_board)
                print()
                print("Game Over")
                print("" + turn + " won the game! Awesome job :)")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':  # down the right side
                print_board(the_board)
                print()
                print("Game Over")
                print("" + turn + " won the game! Awesome job :)")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':  # diagonal
                print_board(the_board)
                print()
                print("Game Over")
                print("" + turn + " won the game! Awesome job :)")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':  # diagonal
                print()
                print("Game Over")
                print("" + turn + " won the game! Awesome job :)")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print()
            print("Game Over. Not too bad, maybe better luck time.")
            print("It was a tie")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.


def main():
    game()
    while input("Play Again? (Y/N): ").upper() == "Y":
        for key in board_keys:
            the_board[key] = " "


main()
