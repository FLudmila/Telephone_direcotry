from Contact_Processing import Add_contact, Delete_contact, Sort_base_id
from File_handling import write_con, read_con
from Display_Contacts import Print_contacts


def User_Comand(base):
    comand = int(input('\n============== МЕНЮ ==============\n'
                       '| 1 - Добавить контакт вручную   |\n'
                       '| 2 - Добавить контакты из файла |\n'
                       '| 3 - Удалить контакт            |\n'
                       '| 4 - Запись справочника в файл  |\n'
                       '| 5 - Вывод справочника на экран |\n'
                       '| 6 - Найти контакт              |\n'
                       '| 0 - Закончить работу           |\n'
                       '==================================\nВыберите режим: '))
    if comand == 1:
        contact = Add_contact()
        contact.insert(0, len(base) + 1)
        base.append(contact)
        return comand, *base
    elif comand == 2:
        try:
            base_from_file = read_con(input('Введите имя файла: '))
            for elem in base_from_file:
                base.append(elem)
            base = Sort_base_id(base)
        except:
            print('[!] Файла с таким именем не существует')
        return comand, *base
    elif comand == 3:
        base = Delete_contact(base)
        base = Sort_base_id(base)
        return comand, *base
    elif comand == 4:
        write_con(base, input('Введите имя файла с раширением: '))
        return comand, *base
    elif comand == 5:
        Print_contacts(base)
        return comand, *base
    elif comand == 0:
        return comand, *base
    else:
        print('Неправильный режим')
