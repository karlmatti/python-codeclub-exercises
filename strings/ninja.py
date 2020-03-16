
def identify_ninja(ninja_name, all_villagers):
    ninja_name = sorted(ninja_name)
    list_of_ninjas = list()
    for alt in all_villagers:
        if ninja_name == sorted(alt):
            list_of_ninjas.append(alt)
    return list_of_ninjas
