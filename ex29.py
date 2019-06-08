board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

user1_wins = 0
user2_wins = 0
emptySpaces = 9
user1_turn = True # user 1 is X, user 2 is O

def hasWon(game):
    # check rows
    for row in range(len(game)):
        global user1_wins, user2_wins
        if game[row][0] == game[row][1] and game[row][1] == game[row][2] and game[row][0] != 0:
            print('User ' +  ('1' if game[row][0] == 'X' else '2') + ' has won!')
            if game[row][0] == 'X':
                user1_wins += 1
            else:
                user2_wins += 1
            return True
    # check columns
    for col in range(len(game)):
        if game[0][col] == game[1][col] and game[1][col] == game[2][col] and game[0][col] != 0:
            print('User ' +  ('1' if game[0][col] == 'X' else '2') + ' has won!')
            if game[0][col] == 'X':
                user1_wins += 1
            else:
                user2_wins += 1
            return True
    # check diagonal
    if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] != 0:
        print('User ' +  ('1' if game[0][0] == 'X' else '2') + ' has won!')
        if game[0][0] == 'X':
            user1_wins += 1
        else:
            user2_wins += 1
        return True

    # check cross diagonal
    if game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[0][2] != 0:
        print('User ' +  ('1' if game[0][2] == 'X' else '2') + ' has won!')
        if game[0][2] == 'X':
            user1_wins += 1
        else:
            user2_wins += 1
        return True
    return False

def drawBoard(list):
    for i in range(3):
        print(' ---' * 3)
        row = ''
        for j in range(3):
            if list[i][j] == 'X':
                row += '| X '
            elif list[i][j] == 'O':
                row += '| O '
            else:
                row += '|   '
        print(row + '|')
    print(' ---' * 3)

while emptySpaces > 0:
    coordinate1 = -1
    coordinate2 = -1
    print('User {}, it\'s your turn!'.format(1 if user1_turn else 2))
    # ask user for coordinates
    while (coordinate1 > 3 or coordinate1 < 1):
        try:
            coordinate1 = int(raw_input('Enter coordinate 1: '))
        except ValueError:
            print('Invalid input')
    while (coordinate2 > 3 or coordinate2 < 1):
        try:
            coordinate2 = int(raw_input('Enter coordinate 2: '))
        except ValueError:
            print('Invalid input')
    # check if board position is already taken
    if board[coordinate1 - 1][coordinate2 - 1] != 0:
        print('Position {}, {} is already taken'.format(coordinate1, coordinate2))
    elif user1_turn:
        board[coordinate1 - 1][coordinate2 - 1] = 'X'
        user1_turn = not user1_turn
        emptySpaces -= 1
    else:
        board[coordinate1 - 1][coordinate2 - 1] = 'O'
        user1_turn = not user1_turn
        emptySpaces -= 1
    # check if someone has won
    drawBoard(board)
    print(board)
    if hasWon(board):
        input = raw_input('Continue? y/n ')
        if input == 'y':
            emptySpaces  = 9
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            user1_turn = True
        else:
            print('User 1 wins: {}, user 2 wins: {}'.format(user1_wins, user2_wins))
            break
