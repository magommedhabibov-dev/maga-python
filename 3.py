# 1.
for i in range(1, 101):
    print(i, end=' ')
# 2.
for i in range(2, 101, 2):
    print(i, end=' ')
# 3.
for i in range(100, 0, -1):
    print(i, end=' ')
# 4.
n = int(input("Введите число n: "))
for i in range(1, n + 1):
    totalsum += i
print(f"Сумма чисел от 1 до {n} равна {totalsum}")
# 5.
n = int(input("Введите число n: "))
total_u = 1
for i in range(1, n + 1):
    total_u *= i
print(f"Факториал числа {n} равен {total_u}")
# 6.
n = int(input("Введите число n: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
# 7.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
# 8.
n = int(input("Введите число n: "))
for i in range(1, 1001):
    if i % 3 == 0:
        count1 += 1

print(f"Количество чисел от 1 до 1000, делящихся на 3: {count1}")
# 9.
n = int(input("Введите число n: "))
odd_sum = 0
for i in range(1, n + 1, 2):
    if i % 2 == 1:
        odd_sum += i
print(f"Сумма нечетных чисел от 1 до {n}: {odd_sum}")
# 10.
for i in range(1, 21):
    print(f"Квадрат числа: {i} = {i**2}")