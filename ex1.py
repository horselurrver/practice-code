from datetime import datetime

name = raw_input("What is your name? ")
age = "default"
while not age.isdigit():
    age = raw_input("Why hello, {}. How old are you? ".format(name))
age = int(age)
now = datetime.now()
current_year = now.year

year_100 = current_year + ((100 - age) if age < 100 else -(age - 100))
message = ""
if age > 100:
    message = "You turned 100 in the year " + str(year_100)
else:
    message = "You will turn 100 in the year " + str(year_100)
print(message)

num_repeats = "default"
while not num_repeats.isdigit():
    num_repeats = raw_input("Enter number of copies to print message: ")

for i in range(int(num_repeats)):
    print(message)
