def flatten(iterable):
    gather = []
    for item in iterable:
        if isinstance(item, (list)):
            gather.extend(flatten(item))
        elif item == None:
            continue
        else:
            gather.append(item)
    return gather
