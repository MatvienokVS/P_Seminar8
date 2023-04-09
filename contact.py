# Добавление контакта


def add_contact(*args):
    name = input('Ввведите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    function = input('Введите должность: ')
    file = "telefon_book.csv"
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{name};{tel_number};{function}\n')


add_contact()
