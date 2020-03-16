def smaller_than(number_1, number_2):
    if float(number_1 > number_2):
        return number_2
    elif float(number_2 > number_1):
        return number_1
    else:
        return None