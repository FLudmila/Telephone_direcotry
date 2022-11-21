from Contact_Processing import Add_contact,Delete_contact
from File_handling import write_con
from Display_Contacts import Print_contacts

def comands():
    comand = int(input(f'Введите режим:\n1 - Добавить контакт\n'
                    f'2 - Удалить контакт\n3 - Запись контакта\n'
          f'4 - Вывод всех контактов'))
    return comand

def User_Comand(num):
    if num == 1:
        Add_contact()
    elif num == 2:
        Delete_contact()
    elif num == 3:
        write_con()
    elif num == 4:
        Print_contacts()
    else:
        print('Неправильный  режим')

comands()