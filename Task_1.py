my_int = 2
my_float = 2.2
my_str = "Hello world"
my_list = ['a', '5']
my_tuple = ('b', '4')
my_dict = {'car': 'lambo', 'ball': 'red'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')