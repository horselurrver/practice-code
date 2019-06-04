import re

results = {}

with open('Training_01.txt', 'r') as open_file:
    for line in open_file:
        result = re.search('/\w/(.*)/(.*)',line)
        if result:
            category = result.group(1)
            if category not in results:
                results[category] = 1
            else:
                results[category] = results[category] + 1

print(results)
