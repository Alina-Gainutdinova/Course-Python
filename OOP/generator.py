from sys import getsizeof

gen = (i for i in range(1000))
print(gen)
print(type(gen))
print(getsizeof(gen))

list_1 = [i for i in range(1000)]
print(type(list_1))
print(getsizeof(list_1))

# gen_to_list = list(gen)
# print(getsizeof(gen_to_list))

# dict_ = {k: v for k, v in range(10)}
# print(dict_)
# for g in gen:
#     print(g)
# print(type(g))
