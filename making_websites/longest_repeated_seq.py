def longest_repeated_seq(word):
    maximum = count = 0
    current = ''
    for c in word.lower():
        if c == current:
            count += 1
        else:
            count = 1
            current = c
        maximum = max(count, maximum)
    if maximum == 1:
        return 0
    else:
        return maximum
