def find(search_list, value):
    left, right = 0, len(search_list) -1

    while left <= right:
        index = (left + right) // 2
        if search_list[index] == value:
            return index
        elif search_list[index] > value:
            right = index -1
        else: 
            left = index + 1

    raise ValueError('value not in array')
