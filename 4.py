# 1.
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1
# 2.
c_password = "mukhammed"
while True:
    password = input("Введите пороль: ")
    if password == c_password:
        print("Доступ разрешен")
        break
    print("Неверный пороль!")
# 3.
c_passkey = 0
while True:
    passkey = input("Введите число: ")
    if passkey == c_passkey:
        print("Вы угадали")
        break
    print("Неверное число!")
# 4.
total_sum = 0
while True:
    num = float(input("Введите число, (0 для остановки): "))
    if num == 0:
        break
    total_sum += num
print(f"Сумма всех чисел: {total_sum}")
# 5.
num = abs(int(input("Введите целое число: ")))
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print(f"Количество цифр в числе: {count}")
# 6.
num = abs(int(input("Введите целое число: ")))
digits_sum = 0

while num > 0:
    digits_sum += num % 10  
    num //= 10              

print(f"Сумма цифр числа: {digits_sum}")
# 7.
num = int(input("Введите число: "))
reversed_num = 0

while num > 0:
    last_digit = num % 10
    reversed_num = (reversed_num * 10) + last_digit
    num //= 10

print(f"Развернутое число: {reversed_num}")
# 8.
original_num = int(input("Введите число: ")) 
num = original_num
reversed_num = 0

while num > 0:
    reversed_num = (reversed_num * 10) + (num % 10)
    num //= 10

if original_num == reversed_num:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")
# 9.
import random

secret_number = random.randint(1, 100)
print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    guess = int(input("Ваш вариант: "))
    
    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print("Поздравляю! Вы угадали число! 🎉")
        break 
# 10.
while True:
    num = float(input("Введите положительное число: "))
    
    if num > 0:
        print(f"Спасибо! Вы ввели корректное число: {num}")
        break  
        
    print("Ошибка! Число должно быть больше 0. Попробуйте ещё раз.")
