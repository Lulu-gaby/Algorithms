def is_palindrome(text):
    # приводим всю строку к нижнему регистру (чтобы заглавные и строчные буквы считались одинаковыми)
    # удаляем из строки пробелы (игнорировать пробелы при проверке)
    # разворачиваем строку задом наперёд
    # сравниваем оригинальную строку и перевёрнутую
    # если они равны — это палиндром, возвращаем True
    # иначе — не палиндром, возвращаем False

    text = text.lower()
    text = text.replace(" ", "")
    reversed_text = text[::-1]
    if text == reversed_text:
        return True
    else:
        return False

print(is_palindrome("Madam"))
print(is_palindrome("Hello"))
print(is_palindrome("А роза упала на лапу Азора"))