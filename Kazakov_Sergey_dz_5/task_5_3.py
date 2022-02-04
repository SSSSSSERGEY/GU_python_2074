
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    klasses += [None for i in range(len(tutors) - len(klasses))]
    for tutor in range(len(tutors)):
        yield tutors[tutor], klasses[tutor]


generator = check_gen(tutors, klasses)
print(type(generator))  # добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
