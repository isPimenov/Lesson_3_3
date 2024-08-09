def print_params(a=1, b='строка', c=True):
    print(a,b,c)
print_params()
print_params(2,'текст')
print_params(b=25)
print_params(c = [1,2,3])


values_list = [15, 'sedan' , False]
values_dict = {'a':25 , 'b': 'crossover' , 'c':True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['roadster', [7.75, 3.13]]
print_params(*values_list_2, 42)