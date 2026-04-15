def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Определяем начало алфавита (A или a)
            start = ord('A') if char.isupper() else ord('a')
            # Вычисляем новую букву через остаток от деления
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result

def main():
    print("--- Программа: Шифр Цезаря ---")
    
    while True:
        mode = input("\nВыберите режим (encrypt/decrypt) или 'exit' для выхода: ").lower()
        if mode == 'exit':
            print("Программа завершена. До свидания!")
            break
            
        if mode not in ['encrypt', 'decrypt']:
            print("Ошибка: введите 'encrypt' или 'decrypt'.")
            continue

        text = input("Введите текст: ")
        
        try:
            shift = int(input("Введите сдвиг (число): "))
        except ValueError:
            print("Ошибка: Сдвиг должен быть целым числом!")
            continue

        result = caesar_cipher(text, shift, mode)
        print(f"Результат ({mode}): {result}")

if __name__ == "__main__":
    main()
