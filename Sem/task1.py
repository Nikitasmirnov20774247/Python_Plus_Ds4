# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def numerated_word(tmp):
    tmp = data.split()
    tmp.sort()
    longest = len(max(tmp, key=len))

    for num, i in enumerate(tmp, 1):
        print(f'{num} {i:>{longest}}')

data = input('Введите строку: ')
numerated_word(data)