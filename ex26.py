# content of test_sample.py
# returns the winner: 1 or 2 (-1 for no winner)
def hasWon(game):
    # check rows
    game.sort()
    for row in range(len(game)):
        if game[row][0] == game[row][1] and game[row][1] == game[row][2] and game[row][0] != 0:
            return game[row][0]
    # check diagonal
    if game[0][0] == game[1][1] and game[1][1] == game[2][2]:
        return game[0][0]

    # check cross diagonal
    if game[0][2] == game[1][1] and game[1][1] == game[2][0]:
        return game[0][2]
    return -1


def test_answer():
    # check rows
    game1 = [[1, 1, 0],
	[2, 2, 2],
	[0, 0, 0]]
    assert hasWon(game1) == 2

    # check diagonal
    game2 = [[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1]]
    assert hasWon(game2) == 1

    # check cross-diagonal
    game3 = [[0, 0, 2],
	[0, 1, 0],
	[1, 0, 0]]
    assert hasWon(game3) == -1
