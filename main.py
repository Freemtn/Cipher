'''
input_text = "кафедра систем информатики"
key = [2, 0, 3, 4, 1]
input_text = "abcdefgh"
key = [1, 3, 0, 2]
'''

#Проверка!!!!!!!!!!!!!!!!!
def encrypt():
    input_text = input("Введите текст:\n")
    key = input("Введите ключ через пробел:\n").split()
    for i in range(len(key)):
        key[i] = int(key[i])
    block_size = len(key)
    group = input("Введите количество в символов в группе или ключевое слово 'word' для шифрования по словам:\n")
    if group == 'word':
        input_text = input_text.split()
    else:
        input_text = [input_text[i:i + int(group)] for i in range(0, len(input_text), int(group))]
    output = [" "] * block_size * (-1 * len(input_text) // block_size * -1)
    for i in range(-1 * len(input_text) // block_size * -1):
        for j in range(block_size):
            if j + i * block_size > len(input_text) - 1:
                output[int(key[j]) + i * block_size] = "\0"
            else:
                output[int(key[j]) + i * block_size] = input_text[j + i * block_size]
    print("Вывод: ")
    if group == "word":
        print(" ".join(output))
    else:
        print("".join(output))


def decrypt():
    input_text = input("Введите текст:\n")
    key = input("Введите ключ через пробел:\n").split()
    for i in range(len(key)):
        key[i] = int(key[i])
    block_size = len(key)
    group = input("Введите количество в символов в группе или ключевое слово 'word' для шифрования по словам:\n")
    if group == 'word':
        input_text = input_text.split()
    else:
        input_text = [input_text[i:i + int(group)] for i in range(0, len(input_text), int(group))]
    output = [" "] * block_size * (-1 * len(input_text) // block_size * -1)
    for i in range(-1 * len(input_text) // block_size * -1):
        for j in range(block_size):
            if j + i * block_size > len(input_text) - 1:
                output[j + i * block_size] = "\0"
            else:
                output[j + i * block_size] = input_text[int(key[j]) + i * block_size]
    print("Вывод: ")
    if group == "word":
        print(" ".join(output))
    else:
        print("".join(output))


a = True
while a == True:
    b = int(input("Выберете команду:\n"
                  "1 - Выйти\n"
                  "2 - Зашифровать\n"
                  "3 - Расшифровать\n"))
    if b == 1:
        print("Завершение программы")
        a = False
    elif b == 2:
        encrypt()
    elif b == 3:
        decrypt()
    else:
        print("Некорректный ввод")
