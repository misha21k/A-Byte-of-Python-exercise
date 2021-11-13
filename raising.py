class ShortInputException(Exception):
    """Пользовательский класс исключений."""
    def __init__(self, lenth, atleast):
        Exception.__init__(self)
        self.lenth = lenth
        self.atleast = atleast


try:
    text = input('Введите что-нибудь: ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputException: Длина введённой строки - {0}; \
ожидалось, как минимум, {1}'.format(ex.lenth, ex.atleast))
else:
    print('Не было исключений')
