def is_palindrome(word):
    if len(word) == 1:
        return True
    if word[0] != word[len(word) - 1]:
        return False
    is_palindrome(word[1:-1])
    return True

input = raw_input("Enter a word: ")
print(input)
print(is_palindrome(input))
