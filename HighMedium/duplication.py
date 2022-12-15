
# Duplication removal

data = [1,2,3,1,4,5,6,2]


def remove_dup(duplist1):

    no_dup_list = []
    for element in duplist1:
        if element not in no_dup_list:
            no_dup_list.append(element)
    return no_dup_list

print(remove_dup(data))

