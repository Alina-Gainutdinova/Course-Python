salaries = [2000, 1800, 3100, 4400, 1500]
bonus = float(input('Введите сумму бонуса: '))
promotion = list(map(lambda x: x + bonus, salaries))
print(promotion)
