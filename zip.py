fruit = ['apple', 'orange', 'banana']
count = [10, 6, 20]
common_list = list(zip(fruit, count))
print(common_list)
second_fruit = fruit.copy()
second_fruit.append('lemon')
fruit.append('pineapple')

print(fruit)
print(second_fruit)
