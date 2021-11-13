import time

try:
    f = open('poem.txt', encoding='utf8')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)  # Пусть подождет некоторое время
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла !!')
finally:
    f.close()
    print('(Очистка: закрытие файла)')
