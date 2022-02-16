# вводим марку и модель телефонов
list_phone = input('Введите марку и модель телефона: ').split(", ")

# Создаем пустые списки для iphones и samsungs
iphones = []
samsungs = []

# Сортируем samsungs и iphones в разные списки
for phone_model in list_phone:
    phone, model = phone.split(" ")
    if phone.lower() == 'iphone':
        iphones.append((phone, int(model)))
    elif phone.lower() == 'samsung':
        samsungs.append((phone, int(model)))
    else:
        print(f"{phone_model} not an iphone nor samsung")

# Выводим список iphones и samsungs
print(f'all iPhones - {iphones}') 
print(f'all Sumsungs - {samsungs}')

# Сравниваем каких телефонов больше
yes_or_not = input('Хотите узнать каких телефонов больше?\n> ')

if yes_or_not.lower() == 'да':
    if len(iphones) > len(samsungs):
        print('iPhones more than Samsungs')
    elif len(iphones) < len(samsungs):
        print('Samsungs more than iPhones')
    else:
        print('Одинаковое колличество')

# Сравниваем модели iphones
yes_or_not = input('Хотите узнать самую новую модель iphones?\n> ')

if yes_or_not.lower() == 'да':
    new_models_iphone = []
    for element in iphones:
        a = element[1]
        new_models_iphone.append(a)
        b = max(new_models_iphone)
    if b == a:
        print(element)

# Сравниваем модели samsungs
yes_or_not = input('Хотите узнать самую новую модель Samsung?\n>')

if yes_or_not.lower() == 'да':
    new_models_samsung = []
    for element in samsungs:
        c = element[1]
        new_models_samsung.append(c)
        v = max(new_models_samsung)
    if v == c:
        print(element)
