def remove_duplicates_loop(lst):
    result = []
    for element in lst:
        if element not in result:
            result.append(element)
    return result

def remove_duplicates_set(lst):
    return list(set(lst))
