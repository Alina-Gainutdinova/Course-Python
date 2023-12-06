def filter_list(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))


print(filter_list([2, 5.9, False, 'python', 6, 'Alina'], bool))
