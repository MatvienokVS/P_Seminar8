# Просмотр телефонной книги


# def get_tb():
#     return telefon_book


# if __name__ == "__main__":
telefon_book = []


def show_all():
    file = 'telefon_book.csv'
    with open(file, 'r', encoding='utf-8') as data:
        data.readlines()
        for i in data:
<<<<<<< HEAD
            print(f'Имя {i}')
=======
            print(i)
>>>>>>> fe5572dfe3d5529576d4dbca5bb3e900c2c0f09f

# show_all()
