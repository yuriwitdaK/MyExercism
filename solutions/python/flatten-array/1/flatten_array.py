def flatten(iterable):
    result = []

    for item in iterable:
        if item is None: #deletes null
           continue
        elif isinstance(item, list):#flattens if list
            result.extend(flatten(item))
        else:#appends item to list 
            result.append(item)
    return result    #returns result

