class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Привет! Меня зовут', self.name)


p = Person('Swaroop')
p.sayHi()

# Предыдущие 2 строки можно записать как Person('Swaroop').say_hi()
