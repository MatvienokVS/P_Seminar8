def menu() -> int:
    print('''Menu:
    1: Добавить контакт.
    2: Удалить контакт.
    3: Редактировать контакт.
    4: Поиск контакта.
    5: Просмотр телефонной книги.
    6: Справка.''')
    enter = ''
    while True:
        enter = input('Выберите пункт меню: ')
        if enter.isdigit() and 0 < int(enter) < 7:
            return int(enter)
        else:
            print('Введите верный пункт меню.')


menu()
