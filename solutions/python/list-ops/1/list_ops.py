def append(list1, list2):

    return list1 + list2
    


def concat(lists):
    return sum(lists, [])

def filter(func, lst):
    result = []
    for item in lst:
        if func(item):
            result.append(item)
    return result
    
    


def length(list):
    return len(list)
    pass


def map(func, lst):
    result = []
    for item in lst:
        result.append(func(item))  # wende func auf jedes Element an
    return result
        



def foldl(function, lst, initial):
    acc = initial
    for item in lst:
        acc = function(acc, item)
    return acc


def foldr(function, lst, initial):
    lst.reverse()
    acc = initial
    for item in lst:
        acc = function(acc, item)
    return acc



def reverse(list):
    list.reverse()
    return list
    pass
