import random
guessed = []
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
    print(result)
    return result

def print_word(word):
    result = ''
    for i in range(len(word)):
        if word[i] in guessed:
            result += word[i] + ' '
        else:
            result += '_ '
    print(result)

def guessed_word(word):
    result = ''
    for i in range(len(word)):
        if word[i] in guessed:
            result += word[i]
    return result

print('Welcome to Hangman!')
print('')
word = generateWord()
print_word(word)
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
        print_word(word)
    else:
        print('Incorrect!')
    print(guessed_word(word))
    if guessed_word(word) == word:
        print('Good job! You got it!')
        break
