# Задание 4
# Можно ли при этом не создавать новый список?
def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    hello = 'Привет,'
    wow = '!'
    for line in list_in:
        name = line.split()[-1:]
        name = str(name)[2:-2]
        name = name.title()
        if 'Игорь' == name:
            name_igor = [hello + name + wow]
            continue
        elif 'Марина' == name:
            name_marina = [hello + name + wow]
            continue
        elif 'Николай' == name:
            name_nikolay = [hello + name + wow]
            continue
        else:
            name_aelita = [hello + name + wow]

        list_out = name_igor + name_marina + name_nikolay + name_aelita

        return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)

print(result)