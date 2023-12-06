dictionary = {'name': 'Alina', 'age': 20, 'edu': 'IT',
              'city': 'Tashkent', 'language': 'Python'}


def dict_to_list(info: dict):
    list_with_tuples = []
    for key, value in info.items():
        if type(value) == int:
            list_with_tuples.append((key, value * 2))
        else:
            list_with_tuples.append((key, value))
    return list_with_tuples


print(dict_to_list(dictionary))
