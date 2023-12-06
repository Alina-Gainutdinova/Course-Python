

while True:
    first_num = float(input('Введите 1-его число: '))
    second_num = float(input('Введите 2-его число: '))
    try:
        print(first_num / second_num)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    else:
        yes_or_no = input('Хотите продолжить (yes/no): ')
        if yes_or_no == 'no':
            break
        else:
            continue
