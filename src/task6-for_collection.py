list_of_elements = [1,2,3,4,5,90]

# for el in list_of_elements:
#     el = el * 2
#     print(el)
#     print(list_of_elements)

# for number in range(0, len(list_of_elements)):
#     list_of_elements[number] = list_of_elements[number] * 2
#     print('Номер в массиве {}   отслеживаем измениения в массиве {}'.format(number, list_of_elements))


for number, value in enumerate(list_of_elements):
    #enumerate генерирует на каждой инерации цикла
    #пару чисел: number - это порядковый номер элемена в массиве
    #value - это значение элемента в массиве
    #И index и value будут другими на кажой последующей итерации, то есть изменяться каждый прогон
    list_of_elements[number] = value * 2 #Берет номер эдемена в массиве и умножает значение которое стоит под этим номером в массиве на два
    print('Номер в массиве {}  отслеживаем измениения в массиве {}'.format(number, list_of_elements))


