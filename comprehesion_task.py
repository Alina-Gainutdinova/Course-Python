dict_info = {
    'city': 'tashkent',
    'language': 'python',
    'framework': 'django'
}

dict_with_upper_letters = {k: v.upper() for k, v in dict_info.items()}
print(dict_with_upper_letters)

str_list = ['Alina', 'abc', 's', 'task', 'python', 'git']

new_list = [s for s in str_list if len(s) > 3]
print(new_list)
