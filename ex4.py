input = ''
while not input.isdigit():
    input = raw_input('Enter a number: ')
input = int(input)
for i in range(1, input):
    if input % i == 0:
        print(str(i))
