score = 0
number_of_operations = 0
percentages = 1.5
list_replenish_take_off = []

def replenish(amount: int):
    global score
    global number_of_operations
    global percentages

    print()

    if score >= 5_000_000:
        res = score // 100 * 10
        score -= res
        print(f'Вычтен налог на богатство 10%: {res}')

    if amount % 50 != 0:
        print('Сумма пополнения должна быть кратна 50 у.е.')
        print(f'Сумма на вашем счёте: {score}')
        print(f'Процент списания: {percentages}')
    else:
        score += amount
        number_of_operations += 1
        print(f'Сумма на вашем счёте: {score}')
        print(f'Процент списания: {percentages}')
        text = f'Записано на счёт: {amount}'
        list_replenish_take_off.append(text)

    if number_of_operations == 3:
        if percentages < 100:
            percentages += 3
        
        number_of_operations = 0

def take_off(amount: int):
    global score
    global number_of_operations
    global percentages

    print()

    if score >= 5_000_000:
        res = score // 100 * 10
        score -= res
        print(f'Вычтен налог на богатство 10%: {res}')

    if amount % 50 != 0:
        print('Сумма снятия должна быть кратна 50 у.е.')
        print(f'Сумма на вашем счёте: {score}')
        print(f'Процент списания: {percentages}')
    elif amount > score:
        print('!! Недостаточно денег на счёте !!')
        print(f'Сумма на вашем счёте: {score}')
        print(f'Процент списания: {percentages}')
    else:
        if amount + amount // 100 * percentages < 30:
            score -= amount + 30
            print(f'Сумма на вашем счёте: {score}')
            print(f'Процент списания: {percentages}')
            text = f'Списано со счёта: {amount}'
            list_replenish_take_off.append(text)
        elif amount + amount // 100 * percentages >= 600:
            score -= amount + 600
            print(f'Сумма на вашем счёте: {score}')
            print(f'Процент списания: {percentages}')
            text = f'Списано со счёта: {amount}'
            list_replenish_take_off.append(text)
        else:
            score -= (amount + amount // 100 * percentages)
            print(f'Сумма на вашем счёте: {score}')
            print(f'Процент списания: {percentages}')
            text = f'Списано со счёта: {amount}'
            list_replenish_take_off.append(text)
    
    number_of_operations += 1
    if number_of_operations == 3:
        if percentages < 100:
            percentages += 3
        number_of_operations = 0


def main():
    while True:
        result = 0

        try:
            print('\nГлавное меню банкомата')
            result = int(input('1 - снять деньги со счёта\n\
2 - положить деньги на счёт\n\
3 - выход\n\
Введите пункт меню: '))
        except:
            print('!! Введён не верный пункт меню !!')
        
        if result == 1:
            while True:
                try:
                    amounter = int(input('Введите сумму снятия: '))
                    break
                except:
                    print('!! Требуется цело число !!')
            take_off(amounter)
        
        if result == 2:
            while True:
                try:
                    amounter = int(input('Введите сумму для пополнения счёта: '))
                    break
                except:
                    print('!! Требуется цело число !!')
            replenish(amounter)
        
        if result == 3:
            print(f'Сумма на вашем счёте: {score}')
            print(f'Процент списания: {percentages}')
            print(list_replenish_take_off)
            break

main()