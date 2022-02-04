
def get_uniq_numbers(src: list):
    unique_brands = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            unique_brands.add(el)
        else:
            unique_brands.discard(el)
        tmp.add(el)
    return [[el for el in src if el in unique_brands]]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
