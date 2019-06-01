# Draws tic tac toe gameboard of size m by n
def drawBoard(m, n):
    for i in range(m):
        print(' ---' * n)
        print('|   ' * (n + 1))
    print(' ---' * n)

if __name__ == "__main__":
    drawBoard(1, 1)
