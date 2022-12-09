import sys
sys.path.append('Telephone_Directory')
from User_Interface import User_Comand
sys.path.append(r'Telegram_Bot_Project\connection')
from bot import tg_bot


def main():
    print('Run Telegram')
    tg_bot()
    # try:
    #     mode = int(input('\n1 - Консольный справочник\n2 - Справочник в Телеграм\nВыбрите режим: '))
    # except:
    #     print('[!] Такого режима нет.')
    #     main()
    # else:
    #     if mode == 1:
    #         base = []
    #         while True:
    #             comand = User_Comand(base)
    #             input_comand = comand[0]
    #             if input_comand == 0:
    #                 break
    #     elif mode == 2:
    #         print('Run Telegram')
    #         tg_bot()
    #     else:
    #         print('[!] Такого режима нет.')
    #         main()

if __name__ == '__main__':
    main()