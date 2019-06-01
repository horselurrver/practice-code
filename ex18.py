from random import randint

answer = str(randint(1000, 9999))
user_guess = ''
print('The answer is ' + answer)

while True:
    cow = 0
    bulls = 0
    while len(user_guess) != 4 or not user_guess.isdigit():
        user_guess = raw_input('Enter a four digit number: ')
    if user_guess == answer:
        print(user_guess + ' is the correct answer!')
        break
    for i in range(len(answer)):
        if answer[i] == user_guess[i]:
            cow += 1
        else:
            bulls += 1
    print("{} cows, {} bulls".format(cow, bulls))
    user_guess = ''
