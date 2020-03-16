def even_only(*args):
    return sum(item for item in args if item % 2 == 0)