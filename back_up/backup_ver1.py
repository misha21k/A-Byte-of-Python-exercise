#!/usr/bin/env python3

import os
import time

source = [r'D:\Музыка', r'D:\Судомоделизм']  # Файлы для копирования
target_dir = r'"D:\Программирование\A Byte of Python Резервная копия файлов"'  # Путь для резерва
# Именем для zip-архива служит текущая дата и время
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'  # Имя архива
zip_command = 'rar a {0} {1}'.format(target, ' '.join(source))  # Создание архива

print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
