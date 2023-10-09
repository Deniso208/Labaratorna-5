import locale
import string

locale.setlocale(locale.LC_COLLATE, 'uk_UA.UTF-8')

def remove_punctuation_and_tokenize(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

def contains_ukrainian_and_english_words(words):
    ukrainian_words = False
    english_words = False
    for word in words:
        if any(char.isalpha() for char in word):
            if any(char.isalpha() and ord(char) > 127 for char in word):
                ukrainian_words = True
            else:
                english_words = True
    return ukrainian_words, english_words
try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        first_sentence = file.readline().strip()
except FileNotFoundError:
    print("Файл не знайдено.")
    exit(1)
except Exception as e:
    print(f"Виникла помилка при читанні файлу: {e}")
    exit(1)

print("Перше речення з файлу:")
print(first_sentence)

try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        entire_text = file.read()
except Exception as e:
    print(f"Виникла помилка при читанні файлу: {e}")
    exit(1)

words = remove_punctuation_and_tokenize(entire_text)

ukrainian_words, english_words = contains_ukrainian_and_english_words(words)

ukrainian_sorted_words = sorted([word for word in words if any(char.isalpha() and ord(char) > 127 for char in word)], key=locale.strxfrm)

english_sorted_words = sorted([word for word in words if any(char.isalpha() and ord(char) <= 127 for char in word)], key=locale.strxfrm)

word_count = len(words)

print("\nСлова у тексті (відсортовані за алфавітом):")
if ukrainian_words:
    print("\nУкраїнські слова:")
    for word in ukrainian_sorted_words:
        print(word)
if english_words:
    print("\nАнглійські слова:")
    for word in english_sorted_words:
        print(word)

print("\nЗагальна кількість слів у тексті:", word_count)
