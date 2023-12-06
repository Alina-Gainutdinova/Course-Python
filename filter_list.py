
list_info = ['Alina', 'Azamat', 'Python', 20, 2023, True, 0, 'JS', False]
filtered_list = []


def filter_list(list_for_filter, value_type):
    for value in list_for_filter:
        if type(value) == value_type:
            filtered_list.append(value)
    return filtered_list


print(filter_list(list_info, str))
