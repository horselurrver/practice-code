def isInList(list, item):
    list.sort()
    lower = 0
    middle = (len(list))/2
    higher = len(list) - 1

    while middle != lower and middle != higher:
        print('lower: {}, middle: {}, higher: {}'.format(lower, middle, higher))
        if list[lower] == item or list[higher] == item:
            return True
        if item > list[middle]:
            lower = middle
            middle = (lower + higher)/2
        elif item < list[middle]:
            higher = middle
            middle = (lower + higher)/2
        else:
            return True

    return False

if __name__== "__main__":
    result = isInList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 100)
    print(result)
