input = raw_input("Please enter a list of numbers separated by spaces: ")
input = input.split()
input = [int(element) for element in input if int(element) % 2 == 0]
print("Only even numbers: {}".format(input))
