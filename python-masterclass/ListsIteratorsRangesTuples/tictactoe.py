test_board = [' ']*10
print(test_board)


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


display_board(test_board)


def player_input():
    marker = input("Choose 'X' or 'O': ")
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


print(player_input())







