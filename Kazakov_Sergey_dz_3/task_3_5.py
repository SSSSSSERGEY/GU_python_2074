
import random

def get_jokes(count, not_repeat = None):
    """Возвращает список шуток в количестве count.
       При наличии второго числового аргумента - 10
       в принте вклячается функция предотвращающая повтор
       слов в шутках,количество шуток ограничено
       условиями задачи.(когда каждое слово можно
       использовать только в одной шутке)"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_out = []
    counter = 0
    while counter < count:
        counter += 1
        word_noun = random.choice(nouns)
        word_adverd = random.choice(adverbs)
        word_adjective = random.choice(adjectives)
        if not_repeat == 10:
            list_out.append(f'{word_noun}  {word_adverd}  {word_adjective}\'')
            nouns.remove(word_noun), adverbs.remove(word_adverd), adjectives.remove(word_adjective)
            if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
                list_out = list_out + ["Шутки кончились,"]
                break
        else:
            list_out.append(f'{word_noun}  {word_adverd}  {word_adjective}\'')

    return list_out


print(get_jokes(2, 10))
print(get_jokes(10, ))