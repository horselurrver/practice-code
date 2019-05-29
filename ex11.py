def is_prime(num):
    for i in range(1, num):
        if num % i == 0 and i != 1 and i != num:
            return False
    return True

while True:
    input = raw_input("Enter a number (or exit to exit) ")
    if input == 'exit':
        break
    if input.isdigit():
        isPrime = is_prime(int(input))
        print(input + " is " + ("prime " if isPrime else "not prime"))
