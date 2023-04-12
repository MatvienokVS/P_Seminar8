import menu
import model


# import contact


def start():
    while True:
        enter = menu.menu()
        match enter:
            case 1:
                model.load_file()
            case 2:
                contact = menu.new_contact()
                model.add_contact(contact)
            case 3:
                pb = model.get_tb()
                menu.show_cont(pb, 'привет')
            case 4:
                pass
            case 5:
                menu.show_cont()
            case 6:
                pass
