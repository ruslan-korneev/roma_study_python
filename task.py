# вводим марку и модель телефонов
list_phone = (input('Введите марку и модель телефона: ').split(", "))

# Создаем пустые списки для iPhone и Samsung
iPhone = []
Samsung = []

# Сортируем Samsung и iPhone в разные списки
for ph in list_phone:
    if ph[0].islower() == True:
        ph,model = ph.split(" ")
        iPhone.append((ph,int(model)))
    else:
        ph,model = ph.split(" ")
        Samsung.append((ph,int(model)))

# Выводим список iPhone и Samsung
print('all iPhones - ',iPhone) 
print('all Sumsungs - ',Samsung)

# Спрашиваем у пользователя хочет ли он узнать каких телефонов больше
print('Хотите узнать каких телефонов больше?')
yes_or_not = input('')

# Сравниваем каких телефонов больше
if yes_or_not == 'да' or yes_or_not == 'Да':
    if len(iPhone) > len(Samsung):
        print('iPhones more than Samsungs')
    elif len(iPhone) < len(Samsung):
        print('Samsungs more than iPhones')
    else:
        print('Одинаковое колличество')
elif yes_or_not == 'нет' or yes_or_not == 'Нет':
    ...

# Сравниваем модели iPhone
print('Хотите узнать самую новую модель iPhone?')
yes_or_not = input('')

new_models_iphone = []

if yes_or_not == 'да' or yes_or_not == 'Да':
    for element in iPhone:
        a = element[1]
        new_models_iphone.append(a)
        b = max(new_models_iphone)
    if b == a:
        print(element)
else:
    ...

# Сравниваем модели Samsung
print('Хотите узнать самую новую модель Samsung?')
yes_or_not = input('')

new_models_samsung = []

if yes_or_not == 'да' or yes_or_not == 'Да':
    for element in Samsung:
        c = element[1]
        new_models_samsung.append(c)
        v = max(new_models_samsung)
    if v == c:
        print(element)
else:
    ...