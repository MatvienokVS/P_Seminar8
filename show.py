# Просмотр телефонной книги
telefon_book = []


def get_tb():
    return telefon_book


def show_all():
    file = 'telefon_book.csv'
    with open(file, 'r', encoding='utf-8') as data:
        data.readlines()
        for i in data:
            i = i.strip().split(';')
            telefon_book.append({'name': i[0],
                                 'tel_number': i[1],
                                 'function': i[2]})

# show_all()
