# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 

from decimal import Decimal

def extrasalary(names, salary, extsalary):
    final_dict = {}
    for i in range(len(names)):
        final_dict[names[i]] = Decimal(salary[i]) * Decimal(extsalary[i].replace('%', ''))
    return final_dict

list_of_numes = ['Иван', 'Дмитрий', 'Мария']
list_of_salary = [100, 120, 140]
list_of_extrasalary = ['10.2%', '14.3%', '15.6%']

for name, award in extrasalary(list_of_numes, list_of_salary, list_of_extrasalary).items():
    print(f'{name} => {award}')