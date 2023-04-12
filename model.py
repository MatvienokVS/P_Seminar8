# Просмотр телефонной книги
telefon_book = []


def get_tb():
    return telefon_book


PATH = 'telefon_book.csv'


def load_file():
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        telefon_book.append({'name': contact[0],
                             'telephone': contact[1],
                             'function': contact[2]})


def save_file():
    data = []
    for contact in telefon_book:
        data.append(';'.join([value for value in contact.value()]))
        data = '\n'.join(data)
        with open(PATH, 'w', encoding='UTF-8') as file:
            file.write(data)


def add_contact(contact):
    telefon_book.append(contact)
