# # Функция проверки ввода целого положительного числа:
def digit_check(param):
    try:
        input_number = int(input(param))
        if not (1 <= input_number <= 100):
            raise ValueError
    except ValueError:
        print('<< Введите целое число: от 1 до 100 ! >>')
        input_number = digit_check(param)
    return input_number


#Ввод кол-ва билетов:
print()
num_ticket = digit_check('>> Введите необходимое кол-во билетов: ')
print()

# Сумма к оплате:
total_cost = float(0)

# Цикл ввода возраста посетителей, согласно кол-ву билетов:
for i in range(1, num_ticket + 1):
    num_age = digit_check(f'>> Введите возраст посетителя, билет №{i}: ')

    # Определяем сумму оплаты, согласно шкале возраста:
    if 18 <= num_age < 25:
        total_cost += 990
    elif num_age >= 25:
        total_cost += 1390

# Если в заказе более 3-х билетов, то скидка 10% от общей суммы:
if num_ticket > 3:
    total_cost -= 0.1 * total_cost

# Вывод результата:
print("\n" + "-" * 52)
print(f"Общая сумма к оплате за {num_ticket:2} посетителей : {total_cost} руб.")
print("-" * 52 + "\n")
print("<< Спасибо за покупку! >>")