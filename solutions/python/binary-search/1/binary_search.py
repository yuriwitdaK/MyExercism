def find(search_list, value):
    search_list.sort()
    left = 0
    right = len(search_list)-1

    while left <= right:
        middle = (left + right) //2
        middle_value = search_list[middle]

        if value == middle_value:
           return middle
        elif middle_value > value:
             right = middle -1
        else:
            left = middle +1
        
    raise ValueError("value not in array")