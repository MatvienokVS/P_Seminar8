# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import menu
import show
<<<<<<< HEAD
import controler

if __name__ == "__main__":
    controler.start()

=======
import contact

if __name__ == "__main__":

    enter = menu.menu()
    while True:
        match enter:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                show.show_all()
            case 6:
                pass
>>>>>>> fe5572dfe3d5529576d4dbca5bb3e900c2c0f09f
