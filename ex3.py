input = raw_input("Enter a list of numbers separated by spaces: ")
input_lst = input.split()
input_lst = [int(element) for element in input_lst]

print([element for element in input_lst if element < 5])
