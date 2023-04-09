# Просмотр телефонной книги
telefon_book = []


# def get_tb():
#     return telefon_book


def show_all():
    file = 'telefon_book.csv'
    with open(file, 'r', encoding='utf-8') as data:
        # data.readlines()
        for i in data:
            print(f'{i}')


show_all()
