# 1. Найти сумму всех элементов списка.
def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# 2. Найти максимальный элемент списка без использования max().
def find_max(lst):
    if not lst:
        raise ValueError("Список пуст")

    maximum = lst[0]
    for num in lst[1:]:
        if num > maximum:
            maximum = num
    return maximum

# 3. Найти минимальный элемент без использования min().
def find_min(lst):
    if not lst:
        raise ValueError("Список пуст")

    minimum = lst[0]
    for num in lst[1:]:
        if num < minimum:
            minimum = num
    return minimum

# 4. Посчитать количество чётных чисел в списке.
def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

# 5. Создать новый список только из нечётных элементов.
def odd_numbers(lst):
    result = []
    for num in lst:
        if num % 2 != 0:
            result.append(num)
    return result

# 6. Удалить все отрицательные числа из списка.
def remove_negatives(lst):
    return [num for num in lst if num >= 0]

# 7. Развернуть список без использования reverse().
def reverse_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

# 8. Найти второй по величине элемент списка.
def second_largest(lst):
    if len(lst) < 2:
        raise ValueError("В списке должно быть хотя бы два элемента")

    largest = second = None
    for num in lst:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif second is None or num > second:
            second = num

    if second is None:
        raise ValueError("В списке нет второго по величине элемента")

    return second

# 9. Удалить дубликаты из списка.
def remove_duplicates(lst):
    result = []
    seen = set()
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# 10. Найти общие элементы двух списков.
def common_elements(lst1, lst2):
    result = []
    for num in lst1:
        if num in lst2 and num not in result:
            result.append(num)
    return result


if __name__ == "__main__":
    sample = [5, -3, 8, 2, 8, 9, -1, 7, 2, 10]

    print("Сумма:", find_sum(sample))
    print("Максимум:", find_max(sample))
    print("Минимум:", find_min(sample))
    print("Чётные:", count_even(sample))
    print("Нечётные:", odd_numbers(sample))
    print("Без отрицательных:", remove_negatives(sample))
    print("Разворот:", reverse_list(sample))
    print("Второй максимум:", second_largest(sample))
    print("Без дублей:", remove_duplicates(sample))
    print("Общие элементы:", common_elements(sample, [8, 2, 11, 7, 23]))
