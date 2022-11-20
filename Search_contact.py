

def Search_cont(contact):
    supername = []
    x  = input('Что ищем ? ')
    for items in contact:
        for y in items:
            if x == y :
                supername.append(items)
    return supername

#  input_data = [['b','имя1','84251653654'],
#                ['фамимлия2','имя2','6576573']]