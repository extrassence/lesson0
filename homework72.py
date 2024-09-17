def custom_write(name, text):
    retn = {}
    file = open(name, 'w', encoding = 'utf-8')
    index = 0
    carriage = 0
    for i in text:
        index += 1
        file.write(i + '\n')
        retn[(index, carriage)] = i
        carriage = file.tell()
    return retn

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


