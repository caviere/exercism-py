from unittest import result


def append(list1, list2):
    asd = list1 + list2
    return asd


def concat(lists):
    result = []
    for list in lists:
        for item in list:
            result.append(item)
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result


def length(list):
    count = 0
    for len in list:
        count +=1
    return count

def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    result = initial
    for item in reverse(list):
        result = function(item, result)
    return result


def reverse(list):
    result = []
    for item in list:
        result.insert(0, item)
    return result
