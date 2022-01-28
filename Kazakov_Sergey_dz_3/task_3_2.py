
list = {"one":"один","two":"два","three":"три","four":"четыре","five":"пять","six":"шесть","seven":"семь","eight":"восемь","nine":"девять","ten":"десять",}

def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    if value.istitle():
        value = value.lower()
        value = list.get(value)
        str_out = value.capitalize()
    else:
        str_out = list.get(value)

    return str_out


print(num_translate("one"))
print(num_translate("Eight"))
print(num_translate("three"))
print(num_translate("Six"))
print(num_translate("nin"))