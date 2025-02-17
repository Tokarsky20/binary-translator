def text_to_binary(text):
    binary_values = []
    for char in text:
        if char == ' ':
            binary_values.append('100000')
        else:
            binary_values.append(format(ord(char), '07b'))
    return ' '.join(binary_values)

if __name__ == '__main__':
    message = "Text"
    binary_message = text_to_binary(message)
    print(binary_message)
