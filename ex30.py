dictionary = []
import random

with open('dictionary.txt', 'r') as f:
  line = f.readline()
  while line:
    # do something to the line, for example
    # saving it to disk
    line = f.readline()
    if (len(line) > 2):
        dictionary.append(line[:-1])
random_num = random.randint(0, len(dictionary) - 1)
print(dictionary[random_num])
