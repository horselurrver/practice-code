import json
import re

with open('info.json', 'r') as f:
    info = json.loads(f)
input = raw_input('Please enter a name: ')
if info['name'] == input:
    print('{}\'s birthday is {}'.format(info['name'], info['birthday']))
print('Let\'s add a new person!')
name = raw_input('Please enter a name: ')

birthday = ''
pattern = '[0-9]{2}/[0-9]{2}/[0-9]{4}'

while not re.match(pattern, birthday):
    birthday = raw_input('Please enter a birthday: ')

with open('info.json', 'w') as f:
    json.dump({'name': name, 'birthday': birthday}, f)
