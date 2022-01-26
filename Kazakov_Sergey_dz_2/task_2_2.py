def convert_list_in_str(list_in: list) -> str:
    rezalt_in = []
    for elem in list_in:
        if '+' in elem or '-' in elem:
            rezalt_in.append(f'{elem[0]}"{elem[1:].zfill(2)}"')
        elif elem.isdigit():
            rezalt_in.append(f'"{elem.zfill(2)}"')
        else:
            rezalt_in.append(elem)
            str_out = rezalt_in,' '.join(rezalt_in)
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

result = convert_list_in_str(my_list)
print(result)