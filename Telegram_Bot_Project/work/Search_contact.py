def Search_cont(contacts, request):
    supername = []
    for items in contacts:
        for i in items:
            if request in str(i):
                supername.append(items)
                break
                
    return supername