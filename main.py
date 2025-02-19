def text_to_binary(text):
    binary_values = []
    for char in text:
        binary_values.append(format(ord(char), '08b'))
    return ' '.join(binary_values)


def binary_to_text(binary_text):
    text_values = []
    binary_chars = binary_text.split()

    for binary_char in binary_chars:
        try:
            text_values.append(chr(int(binary_char, 2)))
        except ValueError:
            return "Помилка: Невірний формат бінарного коду!"

    return ''.join(text_values)


if __name__ == "__main__":
    choice = input("Оберіть режим (1 - текст у бінарний, 2 - бінарний у текст): ")

    if choice == "1":
        message = input("Введіть текст: ")
        binary_message = text_to_binary(message)
        print(f"Бінарний код: {binary_message}")

    elif choice == "2":
        binary_message = input("Введіть бінарний код: ")
        decoded_text = binary_to_text(binary_message)
        print(f"Розшифрований текст: {decoded_text}")

    else:
        print("Невірний вибір!")
