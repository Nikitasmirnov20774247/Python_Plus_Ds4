# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def unicode_list(tmp):
    chr_list = []
    set_of_chr = set(tmp)
    for i in set_of_chr:
        chr_list.append(ord(i))
    return sorted(chr_list, reverse=True)

data = input('Введите строку: ')
print(unicode_list(data))