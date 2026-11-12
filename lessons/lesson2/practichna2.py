# Завдання 1
# Користувач вводить суму на рахунку в банку та суму покупки.
#  Виведіть на екран залишок коштів.
# Можете попросити Student Helper допомогти з назвами змінних

num1 = input("Введите сумму на счете в банке: ")
num2 = input("Введите сумму покупки:")

num1 = float(num1)
num2 = float(num2)

total = num1-num2

print("Остаток после покупки", total)

#Завдання 2
#Напишіть програму яка запитує в користувача ціну
#однієї чашки кави(може бути з копійками) та кількість чашок.
#Виведіть суму замовлення

price1cup = input("Цена одной чашки кофе: ")
numofcups= input("Количество чашек:")

price1cup = float(price1cup)
numofcups = int(numofcups)

total_sum_cups = price1cup * numofcups

print("Сумма заказа", total_sum_cups)

#Завдання 3
#Потрібно порахувати площу прямокутника. Але
#програма видає помилку
#width = input("Введіть ширину: ")
#height = input("Введіть висоту: ")
#area = width * height
#print("Площа дорівнює:", area)
#Запустіть код. Самостійно виправте помилку.

#width = input("Введіть ширину: ")
#height = input("Введіть висоту: ")
#area = width * height
#print("Площа дорівнює:", area)

width = input("Введіть ширину: ")
height = input("Введіть висоту: ")
width = int(width)
height =int(height)    #нужно было обозначить переменную int
area = width * height
print("Площа дорівнює:", area)

#Завдання 4
#Ви обідаєте з друзями в ресторані і вирішуєте скільки залишити чайових.
#Користувач вводить суму рахунку та відсоток
#чайових(наприклад 10, 15 чи 20).
#Виведіть чайові та загальну суму на окремих рядках з підписами.

bill= input("Введите сумму счета: ")
percent = input("Введите процент:")
bill= float(bill)
percent =float(percent)
tips = bill * percent / 100
total_restorant = bill + tips
print("Чаевые:", tips)
print("Общая сумма к оплате:",total_restorant)

#Завдання 5
#Потрібно спланувати витрати на поїздку.
#Користувач вводить
#● відстань в км
#● витрати пального на 100 км в літрах
#● ціна 1 л пального
#Виведіть на екран кількість пального та його ціну

distance_in_km = input("расстояние в км:")
fuel_consumption = input("расход топлива на 100 км в литрах:")
liter_price = input("цена 1 л топлива:")

distance_in_km = float(distance_in_km)
fuel_consumption = float(fuel_consumption)
liter_price = float(liter_price)
total_fuel = (distance_in_km / 100) * fuel_consumption
total_fuel_cost = total_fuel * liter_price
print("Количество топлива:", total_fuel, "л")
print("Общая цена топлива:", total_fuel_cost, "грн")

#Завдання 6
#Користувач вводить два числа, програма повинна
#вивести суму, різницю та добуток. Але програма не працює

num1 = int(input("перше число: "))
num2 = int(input("друге число: "))
sum = num1 + num2
difference = num1 - num2         #проблема была в том что все переменные были одинаковые поэтому код выполнял самую первую функцию
product = num1 * num2
print(sum,difference,product)

#Завдання 7
#Ви вирішили покинути ресторан.
#У завданні 4 модифікуйте код так, щоб ще вводилась
#кількість людей і виводило на екран скільки має заплатити кожен(включно з чайовими)

bill= input("Введите сумму счета: ")
percent = input("Введите процент:")
people = input("Введите количество человек:")
bill= float(bill)
percent =float(percent)
people = int(people)
tips = bill * percent / 100
total_restorant = bill + tips
per_person = total_restorant / people
print("Чаевые:", tips)
print("Общая сумма к оплате:",total_restorant)
print("С каждого человека:", per_person)


