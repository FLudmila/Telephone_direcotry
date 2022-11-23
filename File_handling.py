from Contact_Processing import Add_contact


def write_con(contacts, file_name):
  file = open(file_name, 'a', encoding='utf-8')
  for contact in contacts:
    for elem in contact:
      file.write(str(elem) + ';')
    file.write('\n')
  file.close()
  print(f'База успешно записана в "{file_name}".')


def read_con(file_name):
  contacts = []
  with open(file_name, encoding='utf -8') as file:
    while True:
      line = file.readline().rstrip()
      if not line:
        break
      contact = line.split(';')
      contacts.append(contact)
    print(f'База контактов из файла "{file_name}" успешно добавлена.')
  return contacts
