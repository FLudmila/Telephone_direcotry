from Contact_Processing import Add_contact
from File_handling import write_con,reade_con
from Search_contact import Search_cont
from Display_Contacts import Print_contacts
from Contact_Processing import Delete_contact


#a = Add_contact()
b = reade_con()
#c = Search_cont(b)
#Print_contacts(с)
#Delete_contact(b)
delet = Delete_contact(b)
#Print_contacts(delet)
write_con(delet)