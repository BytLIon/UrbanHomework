def custom_write(file_name, strings):

    strings_positions = dict()

    for i in range(len(strings)):

        file = open(file_name, 'a', encoding='utf-8')
        positions = file.tell()
        file.write(str(strings[i]) + "\n")
        file.close()

        strings_positions[(i+1, positions)] = strings[i]

    return strings_positions



if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)