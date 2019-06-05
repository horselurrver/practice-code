primenumbers = []
happynumbers = []
overlap = []
with open('primenumbers.txt', 'r') as open_file:
    for line in open_file:
        primenumbers.append(int(line))

with open('happynumbers.txt', 'r') as open_file:
    for line in open_file:
        happynumbers.append(int(line))

for i in range(min(len(primenumbers), len(happynumbers))):
    if primenumbers[i] in happynumbers:
        overlap.append(primenumbers[i])

print(overlap)
