import random
rand_list = [random.randint(1, 20) for i in range(0, 10)]

list_comprehension_below_10 = [elem for elem in rand_list if elem < 10]

list_comprehension_below_10 = list(filter(lambda x: x < 10, list_comprehension_below_10))