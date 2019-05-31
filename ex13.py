# Returns the nth Fibonnaci number
def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)

def first_n_of_fibonnaci(n):
    for i in range(1, n + 1):
        print(str(fibonnaci(i)))
