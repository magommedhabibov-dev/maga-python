# 1.
num = 0

if num > 0:
    print("Число положительное")
elif num < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# 2.
num = 5
if num % 2 == 0:
    print("Число четное")  
else: 
    print("Число нечетное")

# 3.
num = 7
num1 = 2
if num > num1:
    print(f"{num} больше {num1}")
elif num < num1:
    print(f"{num} меньше {num1}")
else:
    print(f"{num} равно {num1}")

# 4.
num = 10
num1 = 20
num2 = 15
if num > num1 and num > num2:
    print(f"{num} наибольшее число")
elif num1 > num and num1 > num2:
    print(f"{num1} наибольшее число")
else:
    print(f"{num2} наибольшее число")

# 5.
num = 25
if num % 5 == 0 and num % 3 == 0:
    print(f"{num} делится на 5 и на 3")
else:
    print(f"{num} не делится на 5 и на 3")

# 6.
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} високосный год")
else:
    print(f"{year} не високосный год")

# 7.
age = 18
if age < 0:
    print("Неверный возраст")
elif age <= 12:
    print("Ребёнок")
elif age <= 18:
    print("Подросток")
elif age < 60:
    print("Взрослый")
else:
    print("Пенсионер")

# 8.
correct_password = "password123"
correct_login = "user"
password = input("Введите пароль: ")
login = input("Введите логин: ")
if password == correct_password and login == correct_login:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

# 9.
month = 12

if month in (12, 1, 2):
    print("Зима")
elif month in (3, 4, 5):
    print("Весна")
elif month in (6, 7, 8):
    print("Лето")
elif month in (9, 10, 11):
    print("Осень")
else:
    print("Неверный номер месяца")

# 10.
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")


