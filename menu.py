import model


def menu() -> int:
    print('''Menu:
    1: Просмотр телефонной книги.
    2: Добавить контакт.
    3: Удалить контакт.
    4: Редактировать контакт.
    5: Поиск контакта.
    6: Выход.''')
    enter = ''
    while True:
        enter = input('Выберите пункт меню: ')
        if enter.isdigit() and 0 < int(enter) < 7:
            return int(enter)
            # print(enter)
        else:
            print('Введите верный пункт меню.')


# menu()
def show_cont(book: list[dict], message: str):
    if book:
        for n, contact in enumerate(book, 1):
            print(f'{n}.{contact.get("name"):<20}'
                  f'{contact.get("telephone"):<20}'
                  f'{contact.get("function"):<20}')
    else:
        print(message)


def new_contact() -> dict:
    name = input('Введиет имя контакта: ')
    telephon = input('Введиет номер телефона: ')
    function = input('Введиет должность: ')
    return {'name': name, 'telephon': telephon, 'function': function}
