from Contact_Processing import Add_contact


def write_con(contacts, file_name):
  separator = input('Каким символом разделить строки? ')
  file = open(file_name, 'a', encoding='utf-8')
  for contact in contacts:
    for elem in contact:
      file.write(str(elem) + separator)
    file.write('\n')
  file.close()
  print(f'База успешно записана в "{file_name}".')


def read_con(file_name):
  separator = input('Каким символом разделены строки? ')
  contacts = []
  with open(file_name, encoding='utf -8') as file:
    while True:
      line = file.readline().rstrip()
      if not line:
        break
      contact = line.split(separator)
      contacts.append(contact)
    print(f'База контактов из файла "{file_name}" успешно добавлена.')
  return contacts
