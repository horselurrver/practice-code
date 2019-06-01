import string
import random

types = ['upper', 'number', 'lower', 'symbols']
upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
symbols = list(string.punctuation)

def generateUpper():
    return upper[random.randrange(0, len(upper))]
def generateLower():
    return lower[random.randrange(0, len(lower))]
def generateNumber():
    return random.randrange(0, 10)
def generateSymbol():
    return symbols[random.randrange(0, len(symbols))]

while True:
    result = ""
    input = raw_input("Enter a password length or enter quit: ")
    if input == 'quit':
        break
    if input.isdigit():
        length = int(input)
        for i in range(length):
            type = random.randrange(0, 4)
            if type == 0:
                result += str(generateUpper())
            elif type == 1:
                result += str(generateNumber())
            elif type == 2:
                result += str(generateLower())
            else:
                result += str(generateSymbol())
        print(result)
