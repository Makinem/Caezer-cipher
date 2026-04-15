def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result
  
print("Шифр Цезаря")
text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))
mode = input("Выберите режим (encrypt/decrypt): ").lower()
result = caesar_cipher(text, shift, mode)
print("Результат:", result)
