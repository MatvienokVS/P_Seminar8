# Просмотр телефонной книги
telefon_book = []


def get_tb():
    return telefon_book


PATH = 'telefon_book.txt'


def load_file():
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        telefon_book.append({'name': contact[0],
                             'telephone': contact[1],
                             'function': contact[2]})


def save_file():
    global telefon_book
    data = []
    for contact in telefon_book:
        data.append(';'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(contact):
    telefon_book.append(contact)


def del_contact():
    find_string = input("Введите поисковой запрос: ")
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    data_new = []
    for data_str in data:
        if find_string not in data_str:
            data_new.append(data_str)
    file.close()
    file = open('sample.txt', 'w', encoding='UTF-8')
    file.writelines(data_new)
    file.close()
