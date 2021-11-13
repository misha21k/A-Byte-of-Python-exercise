#!/usr/bin/env python3

import os
import zipfile
import time

source = [r'D:\Музыка', r'D:\Судомоделизм\Чертежи']  # Файлы для копирования
target_dir = r'D:\Программирование\A Byte of Python Резервная копия файлов'  # Путь для резерва
# Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем подкаталога в основном каталоге
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла и создаем имя zip-файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Создаем каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)  # создание каталога
    print('Каталог успешно создан', today)

# Создаем zip-архив
archive = zipfile.ZipFile(target, 'w')
# Записываем в архив наши файлы
for dirMain in source:  # Перебор по элементам копируемых директорий
    for dirPath, dirNames, fileNames in os.walk(dirMain):  # Выковыриваем имена файлов из директории
        for fileName in fileNames:
            filePath = dirPath + os.sep + fileName  # Путь к копируемому файлу на компьютере
            # Путь к файлу внутри архива - filePathInArchive
            filePathInArchive = dirMain.split(os.sep)[-1] + os.sep + filePath.lstrip(dirMain)
            archive.write(filePath, filePathInArchive)
archive.close()
print('Резервная копия успешно создана в', target)
