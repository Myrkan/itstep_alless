# Завдання 1
# Користувач вводить число від 1 до 9. Потрібно вивести
# для цього числа таблицю множення.
# Наприклад для 5 це буде:
# 1х5=5
# 2х5=10
# …
# 9х5=45
# 10х5=50
# Якщо користувач ввів неправильне число то
# продовжувати запитувати поки не введе правильне.

while True:
    num = int(input("Введите число: "))

    if num < 0:
        print("Вы ввели неправильное число")
        continue

    break

for i in range(1, 11):
    result = i * num

    print(f"{i} * {num} = {result}")

# Завдання 2
# Користувач вводить свої оцінки поки не введе 0. Після
# чого програма виводить середню оцінку.
# Виправіть помилку в коді

total = 0
count = 0

while True:
    grade = int(input("Введіть оцінку (или 0 для завершения): "))

    if grade == 0:
        break

    total += grade
    count += 1

if count > 0:
    average_grade = total / count
    print(f"Середня оцінка: {average_grade:.2f}")
else:
    print("Оценки не были введены.")

# Завдання 3
# Напишіть простий калькулятор
# Користувач вводить два числа після чого обирає яку дію
# виконати:
# 1. сума
# 2. різниця
# 3. добуток
# 4. частка
# 5. вихід

print("1. сумма")
print("2. разница")
print("3. произведение")
print("4. доля")
print("5. выход")
print()

while True:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    command = int(input("Выберете номер команди: "))

    if command == 5:
        print("Программа завершена")
        break

    if command < 1 or command > 5:
        print("Вы ввели неправильное число")
        continue

    if command == 1:
        result = a + b
    elif command == 2:
        result = a - b
    elif command == 3:
        result = a * b
    else:
        if b == 0:
            print("На ноль делить нельзя")
            continue
        result = a / b

    print(f"Это будет  {result:.2f}")
    print()

New-Item main.py cd module_git