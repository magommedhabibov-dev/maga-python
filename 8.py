# 71
def add_numbers(a, b):
    return a + b


# 72
def is_even(num):
    return num % 2 == 0


# 73
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# 74
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 75
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# 76
def count_vowels(text):
    vowels = "аеёиоуыэюяaeiouy"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


# 77
def reverse_string(text):
    return text[::-1]


# 78
def list_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# 79
def sum_all_arguments(*args):
    return sum(args)


# 80
def create_user_info(**kwargs):
    return kwargs
