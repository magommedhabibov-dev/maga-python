# 1.
name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

# 2. 
age = int(input("Введите ваш возраст: "))
print(f"Через 10 лет вам будет {age + 10} лет.")

# 3. 
first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
print(f"Сумма: {first_number + second_number}")

# 4. 
first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
print(f"Сумма: {first_number + second_number}")
print(f"Разность: {first_number - second_number}")
print(f"Произведение: {first_number * second_number}")
if second_number != 0:
    print(f"Частное: {first_number / second_number}")
else:
    print("На ноль делить нельзя.")

# 5. 
length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))
print(f"Площадь прямоугольника: {length * width}")

# 6.а
radius = float(input("Введите радиус круга: "))
print(f"Площадь круга: {3.14159 * radius ** 2}")

# 7. 
celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Температура в градусах Фаренгейта: {fahrenheit}")

# 8. 
total_seconds = int(input("Введите количество секунд: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours} ч. {minutes} мин. {seconds} сек.")

# 9.
first_value = input("Введите первое значение: ")
second_value = input("Введите второе значение: ")
first_value, second_value = second_value, first_value
print(f"После обмена: первое = {first_value}, второе = {second_value}")

# 10.
value = input("Введите целое число: ")
integer_value = int(value)
float_value = float(value)
string_value = str(value)
print(f"int: {integer_value}, тип: {type(integer_value).__name__}")
print(f"float: {float_value}, тип: {type(float_value).__name__}")
print(f"str: {string_value}, тип: {type(string_value).__name__}")
