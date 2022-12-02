import sys
sys.path.append('Telephone_Directory')
from User_Interface import User_Comand


def main():
    base = []
    while True:
        comand = User_Comand(base)
        input_comand = comand[0]
        if input_comand == 0:
            break

if __name__ == '__main__':
    main()