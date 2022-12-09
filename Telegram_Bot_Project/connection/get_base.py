import os

def get_base():
    contacts = []
    if os.stat('base.txt').st_size == 0:
        return contacts
    else:
        with open('base.txt', 'r', encoding='utf-8') as base:
            separator = ' '
            while True:
                line = base.readline().rstrip()
                if not line:
                    break
                contact = line.split(separator)
                contacts.append(contact)
        return contacts