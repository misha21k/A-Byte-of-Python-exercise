poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
    используй Pyhton
'''

f = open('poem.txt', 'w', encoding='utf8')  # открываем для записи (writing)
f.write(poem)  # записываем текст в файл
f.close()  # закрываем файл

f = open('poem.txt', encoding='utf8')  # если не указан режим, по умолчанию подразумевается режим чтерия (reading)

while True:
    line = f.readline()
    if len(line) == 0:  # Нулевая длина обозначает конец файла (E0F)
        break
    print(line, end='')

f.close()  # Закрываем файл
