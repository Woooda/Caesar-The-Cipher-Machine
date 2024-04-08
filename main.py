import random
import string

def generate_key(length=5):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def key_to_shift(key):
    return sum(ord(char) for char in key) % 33

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for char in text:
        if char.lower() in alphabet:
            index = alphabet.find(char.lower())
            new_index = (index + shift) % 33
            if char.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += char
    return result

def save_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Текст успешно сохранен в файле: {filename}")

def main():
    while True:
        print("""░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░██╗  ████████╗██╗░░██╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗╚═╝  ╚══██╔══╝██║░░██║██╔════╝
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝░░░  ░░░██║░░░███████║█████╗░░
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗░░░  ░░░██║░░░██╔══██║██╔══╝░░
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║██╗  ░░░██║░░░██║░░██║███████╗
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝
                                                                                            
░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝ 
                                                                                                       by HEXO""")
        print("")
        choice = input("\nВыберите действие:\n1. Зашифровать текст\n2. Расшифровать текст\n3. Сохранить зашифрованный текст в файл\n4. Выйти\n")
        if choice == "1":
            key = generate_key()
            print(f"Ваш ключ: {key}. Сохраните его для расшифровки.")
            shift = key_to_shift(key)
            text = input("Введите текст для шифрования: ")
            encrypted_text = caesar_cipher(text, shift)
            print("Зашифрованный текст:", encrypted_text)
        elif choice == "2":
            key = input("Введите ваш ключ: ")
            shift = key_to_shift(key)
            text = input("Введите текст для расшифровки: ")
            decrypted_text = caesar_cipher(text, shift, True)
            print("Расшифрованный текст:", decrypted_text)
        elif choice == "3":
            key = input("Введите ваш ключ: ")
            shift = key_to_shift(key)
            text = input("Введите текст для шифрования: ")
            encrypted_text = caesar_cipher(text, shift)
            filename = input("Введите имя файла для сохранения зашифрованного текста (.txt): ")
            save_to_file(encrypted_text, filename)
        elif choice == "4":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
