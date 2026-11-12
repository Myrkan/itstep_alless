 # STUDENT HELPER https://m365.cloud.microsoft/chat/agent/T_24f1e3a0-e258-7a14-0bd5-924cdf60ec71.f1921175-4d1e-41eb-aead-b2784a0b64c3.gpt.8ee4dbd5-032e-4382-b42a-a2e818dae863/conversation/2e72c784-bf60-4dca-bf7f-fc99470ffe61


# Завдання 1
# Користувач вводить 2 числа, потрібно вивести середнє
# арифметичне. Але програма не працює
# num1 = input("перше число: ")
# num2 = input("друге число: ")
# sum = num1 * num2
# average = sum / 3
# print("Сума:", sum)
# print("Середнє:", average)
# Запустіть код. Самостійно виправте помилку.
# Попросіть виправити помилку Student Helper та
# порівняйте ваші відповіді


num1 = int(input("перше число: "))
num2 = int(input("друге число: "))
sum = num1 * num2
average = (num1 + num2) / 2   #Чтобы найти среднее арифметическое нужно сложить числа, потом разделить полученную сумму на их количество
print("Сума:", sum)
print("Середнє:", average)    #не работало ведь оно считало цифры текстом

# Завдання 2
# Користувач вводить суму в гривнях та курс долара.
# Переведіть гривні в долари та виведіть на екран

uah_amount = float(input("Введите сумму в гривнах:"))
usd_exchange = float(input("Введите курс долара:"))
usd_amount = uah_amount / usd_exchange

print(f"Из {uah_amount} гривен получается {usd_amount:.2f} долларов")

# Завдання 3
# Користувач вводить ціну товару та відсоток знижки.
# Виведіть суму знижки

product_price = float(input("Введите цену товара:"))
discount_percentage = int(input("Введите процент скидки:"))

discount_amount = (product_price * discount_percentage) / 100
final_price = product_price - discount_amount

print(f"С {discount_percentage}% скидкой вы сэкономите {discount_amount} грн, а заплатите за товар: {final_price} грн")

# Завдання 4
# За 1 хв в залежності від того як швидко ви рухаєтесь
# можна спалити різну кількість калорій
#
# Активність              ккал за 1 хв
# Повільна ходьба              3
# Швидка ходьба               4.5
# Легкий біг                   9
#
# Користувач вводить 3 числа: час повільної/швидкої
# ходьби та бігу.
# Напишіть код який обчислює окремо кількість калорій
# спалених під час цих активностей.
# Також виведіть загальну кількість спалених калорій.

slow_walking = float(input("Введите время медленной ходьбы:"))
brisk_walking = float(input("Введите время быстрой ходьбы:"))
easy_running = float(input("Введите время легкого бега:"))

slow_walking_minute = 3 * slow_walking
brisk_walking_minute = 4.5 * brisk_walking
easy_running_minute = 9 * easy_running

all_calories = slow_walking_minute + brisk_walking_minute + easy_running_minute

print(f"За медленную ходьбу вы сожгли {slow_walking_minute} калорий")
print(f"За быструю ходьбу вы сожгли {brisk_walking_minute} калорий")
print(f"За легкий бег вы сожгли {easy_running_minute} калорий")
print(f"Всего вы сожгли {all_calories} калорий")
