import json

data = [json.loads(line) for line in open('info.json').readlines()]
result = {}

for person in data:
    birthday_month = person['birthday'][:2]
    if birthday_month == '01':
        birthday_month = 'January'
    elif birthday_month == '02':
        birthday_month = 'February'
    elif birthday_month == '03':
        birthday_month = 'March'
    elif birthday_month == '04':
        birthday_month = 'April'
    elif birthday_month == '05':
        birthday_month = 'May'
    elif birthday_month == '06':
        birthday_month = 'June'
    elif birthday_month == '07':
        birthday_month = 'July'
    elif birthday_month == '08':
        birthday_month = 'August'
    elif birthday_month == '09':
        birthday_month = 'September'
    elif birthday_month == '10':
        birthday_month = 'October'
    elif birthday_month == '11':
        birthday_month = 'November'
    elif birthday_month == '12':
        birthday_month = 'December'
    if birthday_month in result:
        result[birthday_month] += 1
    else:
        result[birthday_month] = 1

print(result)
