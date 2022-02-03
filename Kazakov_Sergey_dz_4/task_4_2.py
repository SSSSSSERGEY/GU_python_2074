from requests import get


def currency_rates(val):
    counter = 0
    counter1 = 0
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    tex_str = response.text
    tex_str = tex_str.split('><')
    for i in tex_str:
        counter += 1
        if counter == 2:
            for ii in i.split('"'):
                if len(ii) == 10:
                    date = ii
        else:
            char = i[9:-10]
            nomin_l = i[:7]
            valut_l = i[:5]
            if counter1 == 3 and valut_l == 'Value':
                valute = float((i[6:-7]).replace(',', '.'))
                return f'Дата {date}. {nominal} {char1} = {valute} руб.'
            elif counter1 == 2 and nomin_l == 'Nominal':
                nominal = i[8:-9]
                counter1 = 3
            else:
                if char == val.upper():
                    char1 = char
                    counter1 = 2


print(currency_rates('usd'))
print(currency_rates('EUR'))
print(currency_rates('jp'))
