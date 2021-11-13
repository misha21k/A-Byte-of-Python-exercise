import pickle

shopListFile = 'shoplist.data'  # Имя файла, в котором мы сохраним объект
shopList = ['яблоки', 'манго', 'морковь']  # список покупок

# Запись в файл
f = open(shopListFile, 'wb')
pickle.dump(shopList, f)  # помещаем объект в файл
f.close()

del shopList  # Уничтожаем переменную shopList

# Считываем из хранилища
f = open(shopListFile, 'rb')
storedList = pickle.load(f)  # Загружаем объект из файла
print(storedList)
