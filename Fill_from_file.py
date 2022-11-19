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
