from Contact_Processing import Add_contact,Delete_contact
from File_handling import write_con
from Display_Contacts import Print_contacts

def User_Comand(base):
    comand = int(input(f'Введите режим:\n1 - Добавить контакт\n'
                    f'2 - Удалить контакт\n3 - Запись контакта\n'
          f'4 - Вывод всех контактов\n0 - Закончить работу\n'))
    if comand == 1:
        contact = Add_contact()
        contact.insert(0, len(base) + 1)
        print(contact)
        base.append(contact)
        return comand, *base
    elif comand == 2:
        base = Delete_contact(base)
        return comand, *base
    elif comand == 3:
        write_con()
    elif comand == 4:
        Print_contacts(base)
        return comand, *base
    elif comand == 0:
        return comand, *base
    else:
        print('Неправильный  режим')