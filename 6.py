def my_callback_function(argument):
    print('Это колбэк функция')
    print(argument)


def main_function(callback):
    # Выполнение некоторой работы
    """_summary_

    Args:
        callback (function): _description_
    """
    result = 5 + 3

    # Вызов колбэк функции
    callback(result)


# Вызов основной функции и передача колбэк функции
main_function(my_callback_function)
