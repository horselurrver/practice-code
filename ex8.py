import random
possible_answers = ['rock', 'paper', 'scissors']

print("Welcome to Rock Paper Scissors!")
user = ''
lose_tally = 0
win_tally = 0
tie_tally = 0
while True:
    while user not in possible_answers:
        user = raw_input("Please choose rock, paper, or scissors: ")
    computer = possible_answers[random.randint(0, 2)]
    print("Computer chose " + str(computer))
    if user == computer:
        print("'Tis a tie!'")
        tie_tally += 1
    elif user == 'rock':
        if computer == 'paper':
            print("Computer wins! YOU LOSE")
            lose_tally += 1
        else:
            print("Computer loses! YOU WIN")
            win_tally += 1
    elif user == 'paper':
        if computer == 'rock':
            print("Computer loses! YOU WIN")
            win_tally += 1
        else:
            print("Computer wins! YOU LOSE")
            lose_tally += 1
    else: #user is scissors
        if computer == 'rock':
            print("Computer wins! YOU LOSE")
            lose_tally += 1
        else:
            print("Computer loses! YOU WIN")
            win_tally += 1

    user = ''
    play = raw_input("Would you like to continue playing? y/n: ")
    if play == 'n':
        print("You won a total of {} times, lost a total of {} times, and tied a total of {} times".format(win_tally, lose_tally, tie_tally))
        break
