# 1.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

# 2.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

# 3.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return amount
        return "Недостаточно средств или неверная сумма"

# 4.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# 5.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

# 6.
users_list = [User("Анна", 25), User("Иван", 30)]
with open("users.txt", "w", encoding="utf-8") as file:
    for u in users_list:
        file.write(f"{u.name}, {u.age}\n")

# 7.
with open("users.txt", "r", encoding="utf-8") as file:
    lines_count = sum(1 for line in file)

# 8.
def safe_divide_input():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        return num1 / num2
    except ZeroDivisionError:
        return "Ошибка: Нельзя делить на ноль!"
    except ValueError:
        return "Ошибка: Введены некорректные числа!"

# 9.
class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price

    def remove_product(self, name):
        self.products.pop(name, None)

    def show_products(self):
        return "\n".join(f"{k}: {v} руб." for k, v in self.products.items())

# 10.
import os

class ToDoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as f:
            return [line.strip().split(" | ") for line in f]

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for title, status in self.tasks:
                f.write(f"{title} | {status}\n")

    def add_task(self, title):
        self.tasks.append([title, "В процессе"])
        self.save_tasks()

    def show_tasks(self):
        return "\n".join(f"{i}. [{t[1]}] {t[0]}" for i, t in enumerate(self.tasks, 1))

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index][1] = "Выполнено"
            self.save_tasks()
