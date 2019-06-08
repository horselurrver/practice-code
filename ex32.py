import random
dictionary = []

def fill_dictionary():
    with open('dictionary.txt', 'r') as f:
        line = f.readline()
        while line:
            line = f.readline()
            if (len(line) > 2):
                dictionary.append(line[:-1])

def generateWord():
    if len(dictionary) == 0:
        fill_dictionary()
    random_num = random.randint(0, len(dictionary) - 1)
    result = dictionary[random_num]
    # below line prints the answer
    # print(result)
    return result

def print_word(word, guessed):
    result = ''
    for i in range(len(word)):
        if word[i] in guessed:
            result += word[i] + ' '
        else:
            result += '_ '
    print(result)

def guessed_word(word, guessed):
    result = ''
    for i in range(len(word)):
        if word[i] in guessed:
            result += word[i]
    return result

def start_game():
    guessed = []
    incorrect_guesses = 6
    print('Welcome to Hangman!')
    print('')
    word = generateWord()
    print_word(word, guessed)
    while True:
        input = ''
        while True:
            input = raw_input('Guess your letter: ')
            if input.isalpha() and len(input) == 1 and input not in guessed:
                break
            elif input in guessed:
                print('You already guessed that')
            else:
                print('Invalid input')
        guessed.append(input)
        if input in word:
            print_word(word, guessed)
        else:
            print('Incorrect!')
            incorrect_guesses -= 1
            print('You have {} incorrect guesses left'.format(incorrect_guesses))
        if guessed_word(word, guessed) == word:
            print('Good job! You got it!')
            break
        if incorrect_guesses == 0:
            print('GAME OVER')
            break
start_game()
while True:
    cont = raw_input('Continue? y/n ')
    if cont == 'y':
        start_game()
    else:
        break
