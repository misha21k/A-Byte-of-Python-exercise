#!/usr/bin/env python3

import os
import time

source = [r'D:\Музыка', r'D:\Судомоделизм']  # Файлы для копирования
target_dir = r'D:\Программирование\A Byte of Python Резервная копия файлов'  # Путь для резерва
# Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем подкаталога в основном каталоге
now = time.strftime('%H%M%S')

# Создаем каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)  # создание каталога
    print('Каталог успешно создан', today)

target = today + os.sep + now + '.zip'  # Имя zip-файла
zip_command = 'rar a "{0}" {1}'.format(target, ' '.join(source))  # Создание архива

# Запускаем создание резервной копии
print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
