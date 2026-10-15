# 1.
s1 = "Python"
print(len(s1))

# 2.
s2 = "banana"
print(s2.lower().count('a'))

# 3.
s3 = "hello"
print(s3[::-1])

# 4.
s4 = "level"
print(s4.lower() == s4.lower()[::-1])

# 5.
s5 = "Python"
vowels = "aeiouy"
count_vowels = sum(1 for ch in s5.lower() if ch in vowels)
print(count_vowels)

# 6.
s6 = "Python"
consonants = "bcdfghjklmnpqrstvwxyz"
count_consonants = sum(1 for ch in s6.lower() if ch in consonants)
print(count_consonants)

# 7.
sentence = "Python очень удобный язык программирования"
words = sentence.split()
print(len(words))

# 8.
longest = max(words, key=len)
print(longest)

# 9.
s9 = "Hello world from Python"
print(s9.replace(" ", "-"))

# 10.
s10 = "Python is great"
word = "Python"
print(s10.lower().startswith(word.lower()))
