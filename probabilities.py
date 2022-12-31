print("Вероятности генерации при помощи функции randint случайных последовательностей разной длины, состоящих из нулей или единиц")
print()
print("*****")
print()

import probs_module as pm

while True:
    length = int(input("Введите длину общей последовательности цифр (или целое число меньше 1 для выхода из программы): "))

    if length < 1:
        break

    print()

    data = pm.get_random_list(length)

    print("Сгенерированная последовательность:", data)

    print()

    for i in range(1, length+1):
        x = [0] * i
        p = pm.get_prob(data, x)
        if p == 0:
            break
        if i == 1:
            print("Вероятность генерации одного нуля = ", p)
        elif i > 1:
            print("Вероятность генерации", i, "последовательных нулей = ", p)

    for i in range(1, length+1):
        x = [1] * i
        p = pm.get_prob(data, x)
        if p == 0:
            break
        if i == 1:
            print("Вероятность генерации одной единицы = ", p)
        elif i > 1:
            print("Вероятность генерации", i, "последовательных единиц = ", p)

    print()
