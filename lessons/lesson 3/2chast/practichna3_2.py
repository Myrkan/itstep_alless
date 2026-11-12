# Завдання 1
# Користувач вводить свій вік, якщо він працездатного
# віку(18-65) то виведіть фразу «Працездатний/на», інакше
# «Непрацездатний/на»

age = int(input("Введите ваш возраст: "))

if 18 <= age <= 65:
    print("Працездатний/на")
else:
    print("Непрацездатний/на")


# Завдання 2
# До завдання 2 з попереднього заняття добавте додаткову
# перевірку: щоб отримати доступ користувач повинен ще й
# ввести правильний логін secret_login = "AliBaba"

secret_login = input("Введите логин:")
user_password = input("Введите пароль:")

if user_password == "OpenSesame123" and secret_login == "AliBaba":
    print("Доступ разрешен")
else:
    print("доступ заблокирован")

# Завдання 3
# Оформіть чек покупки. Користувач вводить ціну за
# одиницю товару, кількість товару та свій вік.
# Якщо користувач неповнолітній або старший за 65
# років, то застосуйте знижку 15%

unit_price = int(input("Введите цену за единицу товара:"))
quantity = int(input("Введите количество товара: "))
age = int(input("Введите свой возраст:"))

price = unit_price * quantity

if age <=17 or age >=66:
    discount = price * 0.15
    final_price = price - discount
    print(f"Вам товар со скидкой 15%. Размер скидки: {discount:.2f}. Итоговая сумма: {final_price:.2f}")
else:
    print(f"Сумма покупки: {price:.2f}")

# Завдання 4
# Орендувати авто можна лише якщо
# ● у вас є ліцензія
# ● ви повнолітні
# ● ви не потрапляли в дтп
# Оцініть якість написаного коду, спробуйте його
# спростити використавши and\or

age = 23
has_license = "так"
accidents = 0

if age >= 18:                      #не очень удобно читать и много повторений if
    if has_license == "так":
        if accidents == 0:
            print("Оренда дозволена")
        else:
            print("Оренда заборонена")
    else:
        print("Оренда заборонена")
else:
    print("Оренда заборонена")

age = 23
has_license = "так"
accidents = 0

if age >= 18 and has_license == "так" and accidents == 0:
    print("Оренда дозволена")
else:
    print("Оренда заборонена")

# Завдання 5
# В службі доставки діє акційна пропозиція, чи дорожча
# покупка тим більша знижка на доставку
#
# Ціна покупки             Знижка на доставку
#  < 500 грн                   повна ціна
#  500-1000                      -5%
#  1000-2000                     -20%
#  >2000                  доставка безкоштовно

# Напишіть програму яка запитує у користувача ціну
# покупки та виводить загальну вартість(покупки + доставка)
# Базова ціна доставки: 120 грн
# Знижка діє лише на доставку

price = float(input("Введите цену покупки:"))
delivery_base = 120

if price < 500:
    total_cost = price + delivery_base
    print(f"Полная сумма покупки с доставкой: {total_cost} ")
elif 500 <= price <= 1000:
    discount = delivery_base * 0.05
    final_delivery = delivery_base - discount
    total_cost = price + final_delivery
    print(f"Скидка на доставку 5% ({discount:.2f} грн). Итоговая сумма: {total_cost:.2f}")
elif 1000< price <=2000:
    discount = delivery_base * 0.20
    final_delivery = delivery_base - discount
    total_cost = price + final_delivery
    print(f"Скидка на доставку 20% ({discount:.2f} грн). Итоговая сумма: {total_cost:.2f}")
else:
    total_cost = price
    print(f"Доставка бесплатно! Итоговая сумма: {total_cost:.2f}")

