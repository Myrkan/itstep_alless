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
        amount = a + b
        result = amount

    elif command == 2:
        difference = a - b
        result = difference

    elif command == 3:
        product = a * b
        result = product

    else:
        quotient = a / b
        result = quotient

    print(f"Это будет  {result:.2f}")
    print()
