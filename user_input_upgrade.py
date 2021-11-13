def reverse(text):
    return text[::-1]

def is_palindrome(text):
    punctuation = {' ', '?', '!', '.', ',', ':', ';'}
    textWithoutPunctuation = ''
    for char in text:
        if char not in punctuation:
            textWithoutPunctuation += char.lower()
    return textWithoutPunctuation == reverse(textWithoutPunctuation)


something = input('ВВедите текст: ')
if (is_palindrome(something)):
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')
