from random import uniform
def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    list_in = str(list_in).replace('.',' руб ')
    list_in = list_in.replace(',',  ' коп ,')
    list_in = list_in + f' коп]'
    str_out = list_in[:-6]+list_in[-5:]
    return str_out

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)
print('\n')


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in
print(id(my_list), my_list)

result_2 = sort_prices(my_list)
print(["отсортированный результирующий список"])
print(id(result_2), result_2)
print(result_2)
print('\n')


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True)
    print(id(list_in), list_in)
    print(id(list_out), list_out)
    return list_out

result_3 = sort_price_adv(my_list)
print(["список элементов в списке по убыванию"])
print(result_3)
print('\n')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_in = sorted(list_in, reverse=True)
    list_out = list_in[:5]
    list_out = sorted(list_out)
    return list_out

result_4 = check_five_max_elements(my_list)
print(["список из пяти самых больших элементов"])
print(result_4)