# classified_transmit.py

'''
Подсказки:

Допустим в переменной a - содержится наш текст.

.upper() — делает все буквы заглавными - > Например print(a.upper())

[::-1] — переворачивает текст задом наперед

Можно применить оба метода сразу: a.upper()[::-1]

Пример: "привет" → "ТЕВИРП"

'''

text = 'белый'
text = text[::-1]
print(text)


text2 = 'красный'
text2 = text2[::-1].upper()
print(text2)

text3 = 'амид'
text3 = text3[::-1].upper()
print(text3)