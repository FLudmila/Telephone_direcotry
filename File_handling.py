from Contact_Processing import Add_contact


def write_con(contacts):
 file =  open('new_con.txt','a',encoding= 'utf-8')
 try:
  for elem in contacts:
    file.write(f'{str(elem)}\n')
#  file.write(str(f'{contact[0]};{contact[1]};{contact[2]},{contact[3]}'))
#  file.write(str(f'Name : {contacts[0]},Supername : {contacts[1]},namber Phone : {contacts[2]}, Info : {contacts[3]}\n'))
 finally:
  file.close()


def reade_con():
 contact = []
 with open('Base_2.txt',encoding='utf -8') as file:
   st =  file.readlines()
   for line in st:
    in_str = line.split(' ')
    str1 = tuple( i.rstrip() for i in in_str)
    contact.append(str1)
 return contact
