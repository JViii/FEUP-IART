def copy_list(list1):
    list2 = []

    for i in range(0, len(list1)):
        list2.append(list(list1[i]))

    return list2

def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if len(list1[i]) != len(list2[i]):
            return False
        for j in range(len(list1[i])):
            if list1[i][j] != list2[i][j]:
                return False
            
    return True