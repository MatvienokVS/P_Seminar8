import view


def menu() -> int:
    print('''Menu:
    1: Открыть файл.
    2: Сохранить.
    3: Показать контакты.
    4: Создать контакт.
    5: Изменить контакта.
    6: Выход.''')
    enter = ''
    while True:
        enter = input('Выберите пункт меню: ')
        if enter.isdigit() and 0 < int(enter) < 7:
            return int(enter)
            # print(enter)
        else:
            print('Введите верный пункт меню.')


def print_inf(message: str):
    print('\n' + '-' * len(message))
    print('Книга загружена')
    print('-' * len(message) + '\n')


# menu()
def show_cont(book: list[dict], message: str):
    if book:
        for n, contact in enumerate(book, 1):
            print(f'{n}.{contact.get("name"):<15}'
                  f'{contact.get("telephone"):<15}'
                  f'{contact.get("function"):<15}')
    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input('Введите имя контакта: ')
    tel = input('Введите номер телефона: ')
    function = input('Введите должность: ')
    return {'name': name, 'telephon': tel, 'function': function}
