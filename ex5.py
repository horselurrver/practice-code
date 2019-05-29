from random import randrange
lst1 = [randrange(1, 11) for i in range(randrange(1, 11))]
lst2 = [randrange(1, 11) for i in range(randrange(1, 11))]

print(lst1)
print(lst2)

result = []
for i in range(0, min(len(lst1), len(lst2))):
    if lst1[i] in lst2:
        result.append(lst1[i])

print(result)
