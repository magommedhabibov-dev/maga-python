# 61
numbers = (5, 12, 87, 43, 6, 99, 1, 23, 54, 11)
max_value = max(numbers)
print(max_value)

# 62
my_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_set = set(my_list)
print(unique_set)

# 63
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result_63 = set1.intersection(set2)
print(result_63)

# 64
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result_64 = set1.difference(set2)
print(result_64)

# 65
user = {
    "name": "Алексей",
    "age": 25,
    "city": "Ташкент"
}
print(user)

# 66
user["email"] = "alex@example.com"
print(user)

# 67
del user["city"]
print(user)

# 68
text = "hello world"
char_frequency = {}
for char in text:
    char_frequency[char] = char_frequency.get(char, 0) + 1
print(char_frequency)

# 69
sentence = "яблоко банан яблоко апельсин банан яблоко"
words = sentence.split()
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1
print(word_frequency)

# 70
products_prices = {
    "яблоко": 50,
    "банан": 120,
    "апельсин": 90,
    "груша": 110
}
expensive_product = max(products_prices, key=products_prices.get)
print(expensive_product)
