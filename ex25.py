print('Think of a number between 0 and 100')
print('and I\'ll try to guess it!')

high = 100
low = 0
while True:
    guess = round((high + low)/2.0)
    input = raw_input('Is your number higher than, lower than, or equal to ' + str(guess) + '? ')
    if input.lower() == 'high':
        low = guess
    elif input.lower() == 'low':
        high = guess
    elif input.lower() == 'equal':
        break
    else:
        print('Invalid input')


print('YAY! I win')
