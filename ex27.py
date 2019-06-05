board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
emptySpaces = 9
user1_turn = True # user 1 is X, user 2 is O
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
    print(board)
