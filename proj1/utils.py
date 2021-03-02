def copy_list(list1):
    list2 = []

    for i in range(0, len(list1)):
        list2.append(list(list1[i]))

    return list2