list_dict = [{'name': 'Alina', 'year': 20}, {
    'name': 'Azamat', 'year': 21}, {'name': 'Muha', 'year': 10}]
first, second, third = list_dict


def person_initialization(name, year):
    print(f'Ваше имя: {name}, Возраст: {year}')


person_initialization(**first)
person_initialization(**second)
person_initialization(**third)
