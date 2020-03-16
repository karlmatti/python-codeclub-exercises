def list_sum(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum = int(sum + (number * number))
    return sum