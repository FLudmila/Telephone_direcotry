from User_Interface import User_Comand



def main():
    base = []
    try:
        while True:
            comand = User_Comand(base)
            input_comand = comand[0]
            if input_comand == 0:
                break
    except:
        print('Выбран не верный режим повторите снова')

if __name__ == '__main__':
    main()