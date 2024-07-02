def print_params(a=5, b='Alphabet', c=True):
    print(a, b, c)
print_params(6)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [56, 'Copy', True]
values_dict = {'a': 40, 'b': 'Deer', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [67.3, 'Castle']
print_params(*values_list_2, 5)
