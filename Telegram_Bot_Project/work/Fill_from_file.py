def fill_from_file(file_name):
    text = []
    file = open(file_name, encoding = 'utf-8')
    text = file.readlines()
    file.close()
    for i in range(len(text)):
        elem = []
        elem.append(text[i].split(";"))
        # text[i] = elem
    print(elem)

    return text

# fill_from_file('Base_2.txt')
Base = fill_from_file('Base_3.txt')
print(Base[0])
# print(Base[0][1])

# def print_data(data):
#     for i in range(len(data)):
#         print(i)

# def run():
#     data_csv = read_csv_file()
#     data_txt = read_txt_file()
#     print_data(data_csv)  # печать данных
#     print_data(data_txt)

# def print_data(data):
#     for i in range(len(data)):
#         print(i)

# type_file = input('Введите тип использованого файла txt или csv: ')
# if type_file == 'txt':
#     print_data(data_txt)
# elif type_file == 'csv':
#     print_data(data_csv)
# else:
#     print('Некорректный тип файла')
