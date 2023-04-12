# Просмотр телефонной книги


# def get_tb():
#     return telefon_book

telefon_book = []


def show_all():
    file = 'telefon_book.csv'
    with open(file, 'r', encoding='utf-8') as data:
        data.readlines()
        for i in data:
            print(i)


show_all()
