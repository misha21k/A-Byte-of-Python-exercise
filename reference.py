print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist  # mylist - лишь ещё одно имя, указывающее на тот же объект!

del shoplist[0]  # Я сделал первую покупку, поэтому удаляю её из списка

print('shoplist:', shoplist)
print('mylist:', mylist)

print('Копирование при помощи полной вырезки')
mylist = shoplist[:]  # создаем копию путём полной вырезки
del mylist[0]  # удаляем первый элемент

print('shoplist:', shoplist)
print('mylist', mylist)
