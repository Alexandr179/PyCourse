'''
    intro to Python3
    https://levashove.ru/how-to-configure-actions-when-closing-a-cover-in-ubuntu/
      ...это для ubuntu - powerOff_plugin :)
'''


print("---------------------- demo ----------------------")


# >>>>>>>> encoding..
b_world = 'привет'.encode()
print(b_world)

world = b_world.decode('utf8')
print(world)


print(type(world))
print(isinstance(world, str))
# hashCode by alalog.Java..
print(id(world))

# >>>>>>>>  в Str
    # user_input = input('введите координаты: ')

# >>>>>>>> приведение к Int
    # x, y = map(int, input('введите координаты !через пробел: ').split())
    # print(type(x))
    # print(x, y)


# >>>>>>>> работа со строками
rav4 = 'Toyota Rav4'
print('номер символа: ', rav4.find('a'))

# ..см.докумантацию
rav4.replace('а', 'б')



# >>>>>>>> списки       .min/max()  count()   sort()
my_list = ['a', 3, '44']
my_list.append('ssd')

my_list.extend([1,2,3,4])
my_list.insert(2, rav4)
print('My list: ', my_list)

print('третий элемент: ', my_list[3])
del my_list[3]
my_list.remove('ssd')

# ..см.докумантацию
my_list.pop(1)

matrix = [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
print('элемент[1][1] матрицы: ', matrix[1][1])

print('входит ли \'5\' в my_list? ', 5 in my_list)


# >>>>>>>> range  (внимание: список может создаваться, как через [] ,
#                                           так и через конструктор: list() ...)
print(list(range(100)))


# >>>>>>>>  изменеяемые и неизменяемые объекты (str и числовые.. см.лекцию)


# >>>>>>>>  словари
my_box = {}
my_box['слон'] = 'elephant'
my_box['машина'] = 'car'

print('my_box: ', my_box)

my_box = {'1': 'one', '2': 'two'}
print('my_box: ', my_box)

print('наличие.. ', '1' in my_box)
print('наличие.. ', my_box.get('2', 'второй ключ!'))


# множества   ..операции:   my_set | other_set, & -пересечение, '-' вычитание
my_set = {1, 2, 3}
