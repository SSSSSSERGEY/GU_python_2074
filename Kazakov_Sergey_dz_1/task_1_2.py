
def sum_list_1(dataset: list)-> int:
    my_list2 = []
    total_amount = 0  # Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7
    for lis_numbers in dataset:
        number = 0
    #    print(lis_numbers)
        numb_length = list(str(lis_numbers))  # игра с классами для итерации числа
        if (len(numb_length) == 1):  # на всякий случай пропускаем еденичку
           continue
        else:
            counter = 0
            for i in numb_length:  # итерируем одно число из данного списка
                counter += 1
                number = (int(number) + int(i))
                if(counter == (len(numb_length))):  # берём только последнее число от итераций добовляем в список
                    my_list2.append(number)
                #    print(my_list2)

                    if(number % 7 == 0):  # делится без остатка берём значение i
                        total_amount = total_amount + lis_numbers  # это (число списка на момент) и в общую сумму
                        summ = total_amount
    return summ  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    counter = 0                                             # К каждому элементу списка добавляет 17 и вычисляет сумму
    variabl = dataset[-1]  # обман для входа в цикл         # чисел списка, сумма цифр которых делится нацело на 7
    while variabl != dataset[0]:
        counter += 1
        if(counter == 1):  # меняем обманную переменную while после 1 цикла для остановки while 18 == 18 первое число
            variabl = (dataset[0 ]+ 17)  # первое число по кругу +17
            dataset.append(dataset[0] + 17)  # в списке и с собой сравняется к каждому +17 остановка
            del dataset[0]
        else:
            dataset.append(dataset[0] + 17)  # последующие циклы на круг
            del dataset [0]

        if(variabl == dataset[0]):  # всё 18 == 18 пора на раскладку
            my_list2 = []
            total_amount = 0  # Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7
            for lis_numbers in dataset:
                number = 0
         #      print(lis_numbers)  # проверка списка плюс 17
                numb_length = list(str(lis_numbers))  # игра с классами для итерации числа
                if (len(numb_length) == 1):  # на всякий случай пропускаем еденичку
                    continue
                else:
                    counter = 0
                    for i in numb_length:  # итерируем одно число из данного списка
                        counter += 1
                        number = (int(number) + int(i))
                        if (counter == (len(numb_length))):  # берём только последнее число от итераций добовляем в список
                            my_list2.append(number)

                            if (number % 7 == 0):  # делится без остатка берём значение i
                                total_amount = total_amount + lis_numbers  # это (число списка на момент) и в общую сумму
                                summ = total_amount
            return summ  # Верните значение полученной суммы


my_list = []  # Соберите нужный список по заданию

for i in range (1,1000,2):
    numbe_cub = i**3
    my_list.append(numbe_cub)

result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)
