nums = [-2, 10, 56, 9, -3, 0]

even_nums = [num for num in nums if num % 2 == 0]

print(even_nums)

all_nums = {num * num for num in range(10)}
print(all_nums)
print(type(all_nums))

my_scores = {
    'a': 10,
    'b': 7,
    's': 14
}

scores = {k: v * 10 for k, v in my_scores.items()}
print(scores)


nums_2 = {index: elem for index, elem in enumerate(nums)}
print(nums_2)
