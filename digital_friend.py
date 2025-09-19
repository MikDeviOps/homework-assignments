


health = 100        # int - целое число
name = "Владимир"       # str - строка (текст)
key = False       # bool - True или False
gold = 1          # float - дробное число


if key == True: 
    print('дверь открыта ключом')
elif health < 80:
    print('дверь закрыта') 
elif gold >= 80:
    print('дверь открывается')
else:
    print('закрыто')