import random

def game(num):
    user = ''
    print("The number is {}".format(num))
    while not user.isdigit() or int(user) < 0 or int(user) > 100:
        user = raw_input("Please enter an integer between 0 and 100 inclusive (or exit to exist): ")
        if user == 'exit':
            print("Thanks for playing!")
            exit()
    user = int(user)
    if user == num:
        print("Congratulations! You correctly guessed {}".format(user))
        exit()
    elif user < num:
        print("Your guess of {} is a little low".format(user))
    else:
        print("Your guess of {} is a little high".format(user))
    user = ''

num = random.randint(0, 100)
while True:
    game(num)
