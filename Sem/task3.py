# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def two_numbers_unicode(data):
    unicod_dict = {}
    num_1, num_2 = map(int, data.split())
    
    if num_1 > num_2: 
        num_1, num_2 = num_2, num_1
    for i in range(num_1, num_2 + 1, 1):
        unicod_dict[i] = chr(i)
    return unicod_dict

data = input('Введите строку: ')
print(two_numbers_unicode(data))