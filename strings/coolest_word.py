def coolest_word(words):
    dict = {}
    for word in words:
        unique = []
        for char in word[::]:
            if char not in unique:
                unique.append(char)
        dict[word] = len(unique)
    if dict:
        return max(dict, key=dict.get)
    else:
        return None
