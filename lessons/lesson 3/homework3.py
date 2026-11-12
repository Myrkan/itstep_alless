# STUDENT HELPER
# https://m365.cloud.microsoft/chat/agent/T_24f1e3a0-e258-7a14-0bd5-924cdf60ec71.f1921175-4d1e-41eb-aead-b2784a0b64c3.gpt.8ee4dbd5-032e-4382-b42a-a2e818dae863/conversation/65b3599d-05f9-407f-8d04-be7889d52c5b


# Завдання 1,
# Щоб створити одну глиняну фігурку треба 130 грамів
# глини.
# Користувач вводить масу глини в кілограмах. Виведіть
# скільки фігурок він зможе зробити.
# Наприклад, з 2 кг глини можна зробити 15 фігурок
# Розтавте команди нижче у правильному порядку та
# додайте підписи з описом що робить команда(є
# продовження на наступній сторінці)


clay = float(input("Введіть масу глини(кг): "))

clay_per_figure = 130
clay *= 1000
figures = clay // clay_per_figure

print(f"Можна зробити: {figures} фігурок")

# Завдання 2
# Троє друзів пішли на рибалку. Програма отримує кількість риби яку зловив кожен рибалка.
# Виведіть на екран:
# ● скільки в середньому вийшло риб на людину
# ● розмір найбільшого улову

first_fisherman = int(input("Введите количество пойманной рыбы для первого рыбака:"))
second_fisherman = int(input("Введите количество пойманной рыбы для второго рыбака:"))
third_fisherman = int(input("Введите количество пойманной рыбы для третьего рыбака:"))

average = (first_fisherman  + second_fisherman + third_fisherman) / 3
largest = max(first_fisherman,second_fisherman,third_fisherman)

print(f"Средний улов на рыбака: {average:.2f} рыб")
print(f"{largest} рыб - самый большой улов")

# Завдання 3
# У кінотеатрі можна замовити квитки онлайн
#
#    Місце                          Ціна
#   Звичайне                       150 грн
#     VIP                          250 грн
#
# Користувач вводить бюджет. Виведіть скільки людей
# може піти в кіно якщо купляти лише звичайні місця або лише VIP

budget = float(input("Введите ваш бюджет:"))

price_regular = 150
price_vip = 250

people_regular = budget // price_regular
people_vip = budget // price_vip

print(f"На обычные места (150 грн) хватит на {people_regular} человек")
print(f"На VIP места (250 грн) хватит на {people_vip} человек")


# Завдання 7 С практической
# Користувач вводить суму вкладу в банк та відсоток ставки.
# ● Обчисліть скільки користувач отримує через 5 років,
# якщо кожного року сума вкладу збільшується на даний відсоток
# ● Виведіть суму вкладу кожного року окремо


amount_deposit = float(input("Введите начальную сумму вклада:"))

rate_percent = float(input("Введите годовой процент:"))

rate = rate_percent / 100

first_year  = amount_deposit * (1 + rate)
second_year = first_year * (1 + rate)
third_year  = second_year * (1 + rate)
fourth_year = third_year * (1 + rate)
five_year   = fourth_year * (1 + rate)

print(f"Сумма вклада после 1 года: {first_year:.2f}")
print(f"Сумма вклада после 2 года: {second_year:.2f}")
print(f"Сумма вклада после 3 года: {third_year:.2f}")
print(f"Сумма вклада после 4 года: {fourth_year:.2f}")
print(f"Сумма вклада после 5 года: {five_year:.2f}")


# Завдання 4
# Користувач вводить суму грошей.
# Програма розкладає суму на:
# ● купюри по 500;
# ● купюри по 200;
# ● купюри по 100;
# ● решту.

# Введіть суму грошей: 1630
# Купюр по 500: 3
# Купюр по 200: 0
# Купюр по 100: 1
# Решта: 30

total_uah = int(input("Введите сумму денег:"))

count_500 = total_uah // 500
rem_after_500 = total_uah % 500

count_200 = rem_after_500 // 200
rem_after_200 = rem_after_500 % 200

count_100 = rem_after_200 // 100
rem_after_100 = rem_after_200 % 100

# Просто выводим все строки подряд
print(f"Сумма {total_uah} грн разложена на:")
print(f"- {count_500} купюр по 500 грн")
print(f"- {count_200} купюр по 200 грн")
print(f"- {count_100} купюр по 100 грн")
print(f"- и ещё осталось {rem_after_100} грн")
