import re


def hex_to_rgb(string):

    lv = len(string)
    match = re.search(r'(?:[0-9a-fA-F]{3}){1,2}$', string)

    if match and lv == 6:
        return list(int(string[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    else:
        return []


string = "ff99000"
print(str(hex_to_rgb(string)))

