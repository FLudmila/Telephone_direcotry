from Contact_Processing import Add_contact


def write_con(contacts, file_name='telephone_directory.txt'):
  file = open(file_name, 'a', encoding='utf-8')
  try:
    for elem in contacts:
      file.write(f'{str(elem)}\n')
  finally:
    file.close()


def read_con(file_name):
  contacts = []
  with open(file_name, encoding='utf -8') as file:
    while True:
      line = file.readline().rstrip()
      if not line:
        break
      contact = line.split(';')
      contacts.append(contact)
  return contacts
