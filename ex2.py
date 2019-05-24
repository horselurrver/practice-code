num = ""
while not num.isdigit():
    num = raw_input("Enter a number: ")
num = int(num)
if num % 4 == 0:
    print(str(num) + " is divisible by 4")
elif num % 2 == 0:
    print(str(num) + " is even")
else:
    print(str(num) + " is odd")

divisor = ""
dividend = ""
while not divisor.isdigit():
    divisor = raw_input("Enter a divisor: ")
while not dividend.isdigit():
    dividend = raw_input("Enter a dividend: ")

if int(divisor) % int(dividend) == 0:
    print(dividend + " divides evenly into " + divisor)
else:
    print(dividend + " does not divide evenly into " + divisor)
