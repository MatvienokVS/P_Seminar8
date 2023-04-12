import view
import model


def start():
    while True:
        enter = view.menu()
        match enter:
            case 1:
                model.load_file()
                view.print_inf('Книга загружена')
            case 2:
                model.save_file()
            case 3:
                pb = model.get_tb()
                view.show_cont(pb, 'Привет')
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
            case 5:
                pass
            case 6:
                pass
