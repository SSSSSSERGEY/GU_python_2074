
def thesaurus(*args) -> dict:
    dict_out = {}
    for names in range(len(args)):
        name = args[names]
        initials = name[0]
        name2 = args[names]
        name1 = dict_out.setdefault(initials, [name2])
        if [name2] != name1:
            name2 = [name2]
            dict_out[initials] = (name1 + name2)

    return dict(sorted(dict_out.items()))


print(thesaurus("Петр", "Илья", "Мария", "Борис", "Иван"))