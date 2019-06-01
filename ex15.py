input = raw_input("Enter a string containing multiple words: ")
in_order = input.split()
backwards_order = [in_order[len(in_order) - 1 - i] for i in range(len(in_order))]
result = " ".join(backwards_order)
print(result)
