from User_Interface import User_Comand

base = []
while True:   
    comand = User_Comand(base)
    input_comand = comand[0]
    if input_comand == 0:
        break