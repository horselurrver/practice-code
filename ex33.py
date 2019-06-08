def print_names(dict):
    for key in dict:
        print key

dictionary = {'Amy Wang': '11/11/1999'}
print('Welcome to the birthday dictionary. We know the birthdays of: ')
print_names(dictionary)
input = raw_input('Whose birthday do you want to look up? ')
if input in dictionary:
    print(input + '\'s birthday is ' + dictionary[input])
