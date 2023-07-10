# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
## ✔ Если индекс выходит за пределы списка, сумма считается
## до конца и/или начала списка.

def two_numbers(num_1, num_2, tmp):
    s = 0
    if num_1 > num_2: 
        num_1, num_2 = num_2, num_1
    for i in tmp[num_1 + 1: num_2]:
        s += i
    return s

list_of_numbers = [4, 1, 5, 12, 2, 6, 7, 8]
index_1 = 3
index_2 = 7
print(two_numbers(index_1, index_2, list_of_numbers))