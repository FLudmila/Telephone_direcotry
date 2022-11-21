from Search_contact import Search_cont
from Display_Contacts import Print_contacts


def Add_contact():
    contact  = []
    name = input('Введите имя контакта - ')
    contact.append(name)
    supername = input('Введите фамилию контакта - ')
    contact.append(supername)
    try:
        number_phone = int(input('Введите номер телефона - '))
    except:
        number_phone = int(input('[!] Номер должен содержать только цифры. Введите номер телефона - '))
    contact.append(number_phone)
    info = input('Введите информацию о контакте - ')
    contact.append(info)
    print(f'{contact} Контакт добавлен\n')
    return contact


def Delete_contact(base):
    contact = Search_cont(base)
    if len(contact) == 0:
        print('Такого контакта нет ')
    else:
        if len(contact) == 1:
            base.pop(int(contact[0][0])-1)
            print(f'{contact[0]}\n Этот контакт удалён')
        elif len(contact) > 1:
            Print_contacts(contact)
            choose_contact = int(input('Найдено несколько контактов,какое id удалить - '))
            base.pop(int(contact[choose_contact - 1][0])-1)
            print(f'{contact[choose_contact - 1]}\n Этот контакт удалён')
        for id in range(len(base)):
            base[id][0] = id + 1

        
        
    return base