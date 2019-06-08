import json
import re

data = [json.loads(line) for line in open('info.json').readlines()]

def addPerson():
    birthday = ''
    pattern = '[0-9]{2}/[0-9]{2}/[0-9]{4}'

    print('Let\'s add a new person!')
    name = raw_input('Please enter a name: ')

    while not re.match(pattern, birthday):
        birthday = raw_input('Please enter a birthday: ')

    with open('info.json', 'a') as f:
        json.dump({'name': name, 'birthday': birthday}, f)

def findPerson():
    input = raw_input('Please enter a name: ')
    for person in data:
        if person['name'] == input:
            print('{}\'s birthday is {}'.format(person['name'], person['birthday']))

while True:
    input = (raw_input('Would you like to add, find, or quit? ')).lower()
    if input == 'add':
        addPerson()
    elif input == 'find':
        findPerson()
    else:
        break
